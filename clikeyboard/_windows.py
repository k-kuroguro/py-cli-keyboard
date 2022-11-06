import msvcrt
import sys
from ctypes import Structure, Union, WinDLL, byref
from ctypes.wintypes import BOOL, CHAR, DWORD, HANDLE, SHORT, UINT, WCHAR, WORD
from typing import IO, Any, Callable, Optional

# Adapted from Textual https://github.com/Textualize/textual/blob/main/src/textual/drivers/win32.py.
# See ./Textual_LICENSE.


class COORD(Structure):
    '''https://docs.microsoft.com/en-us/windows/console/coord-str'''

    _fields_ = [
        ('X', SHORT),
        ('Y', SHORT)
    ]


class uChar(Union):
    '''https://docs.microsoft.com/en-us/windows/console/key-event-record-str'''

    _fields_ = [
        ('UnicodeChar', WCHAR),
        ('AsciiChar', CHAR)
    ]


class KEY_EVENT_RECORD(Structure):
    '''https://docs.microsoft.com/en-us/windows/console/key-event-record-str'''

    _fields_ = [
        ('bKeyDown', BOOL),
        ('wRepeatCount', WORD),
        ('wVirtualKeyCode', WORD),
        ('wVirtualScanCode', WORD),
        ('uChar', uChar),
        ('dwControlKeyState', DWORD)
    ]


class MOUSE_EVENT_RECORD(Structure):
    '''https://docs.microsoft.com/en-us/windows/console/mouse-event-record-str'''

    _fields_ = [
        ('dwMousePosition', COORD),
        ('dwButtonState', DWORD),
        ('dwControlKeyState', DWORD),
        ('dwEventFlags', DWORD)
    ]


class WINDOW_BUFFER_SIZE_RECORD(Structure):
    '''https://docs.microsoft.com/en-us/windows/console/window-buffer-size-record-str'''

    _fields_ = [
        ('dwSize', COORD)
    ]


class MENU_EVENT_RECORD(Structure):
    '''https://docs.microsoft.com/en-us/windows/console/menu-event-record-str'''

    _fields_ = [
        ('dwCommandId', UINT)
    ]


class FOCUS_EVENT_RECORD(Structure):
    '''https://docs.microsoft.com/en-us/windows/console/focus-event-record-str'''

    _fields_ = [
        ('bSetFocus', BOOL)
    ]


class InputEvent(Union):
    '''https://docs.microsoft.com/en-us/windows/console/input-record-str'''

    _fields_ = [
        ('KeyEvent', KEY_EVENT_RECORD),
        ('MouseEvent', MOUSE_EVENT_RECORD),
        ('WindowBufferSizeEvent', WINDOW_BUFFER_SIZE_RECORD),
        ('MenuEvent', MENU_EVENT_RECORD),
        ('FocusEvent', FOCUS_EVENT_RECORD)
    ]


class INPUT_RECORD(Structure):
    '''https://docs.microsoft.com/en-us/windows/console/input-record-str'''

    _fields_ = [
        ('EventType', WORD),
        ('Event', InputEvent)
    ]


_WAIT_TIMEOUT = 0x00000102

# Console input modes
_ENABLE_ECHO_INPUT = 0x0004
_ENABLE_EXTENDED_FLAGS = 0x0080
_ENABLE_INSERT_MODE = 0x0020
_ENABLE_LINE_INPUT = 0x0002
_ENABLE_MOUSE_INPUT = 0x0010
_ENABLE_PROCESSED_INPUT = 0x0001
_ENABLE_QUICK_EDIT_MODE = 0x0040
_ENABLE_WINDOW_INPUT = 0x0008
_ENABLE_VIRTUAL_TERMINAL_INPUT = 0x0200

# Console output modes
_ENABLE_PROCESSED_OUTPUT = 0x0001
_ENABLE_WRAP_AT_EOL_OUTPUT = 0x0002
_ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
_DISABLE_NEWLINE_AUTO_RETURN = 0x0008
_ENABLE_LVB_GRID_WORLDWIDE = 0x0010

_STD_INPUT_HANDLE = -10
_STD_OUTPUT_HANDLE = -11

_MAX_EVENTS = 1024
_KEY_EVENT = 0x0001

_kernel32 = WinDLL('kernel32', use_last_error=True)

_GetStdHandle = _kernel32.GetStdHandle
_GetStdHandle.argtypes = [DWORD]
_GetStdHandle.restype = HANDLE
_ReadConsoleInputW = _kernel32.ReadConsoleInputW
_WaitForMultipleObjects = _kernel32.WaitForMultipleObjects
_SetConsoleMode = _kernel32.SetConsoleMode
_GetConsoleMode = _kernel32.GetConsoleMode

_hIn = _GetStdHandle(_STD_INPUT_HANDLE)
_arrtype = INPUT_RECORD * _MAX_EVENTS
_input_records = _arrtype()
_read_count = DWORD(0)
_keys: list[str] = []


def _wait_for_handles(handles: list[HANDLE], timeout: int = 0) -> Optional[HANDLE]:
    '''http://msdn.microsoft.com/en-us/library/windows/desktop/ms687025(v=vs.85).aspx'''

    arrtype = HANDLE * len(handles)
    handle_array = arrtype(*handles)

    ret: int = _WaitForMultipleObjects(
        len(handle_array), handle_array, BOOL(False), DWORD(timeout)
    )

    if ret == _WAIT_TIMEOUT:
        return None
    else:
        return handles[ret]


def listen(handler: Callable[[list[str]], None]) -> None:
    '''
    Listen key press events.

    Args:
        handler (Callable[[list[str]], None]): A callable fired when key pressed.
    '''

    if _wait_for_handles([_hIn], 200) is None:
        return

    _ReadConsoleInputW(
        _hIn, byref(_input_records), _MAX_EVENTS, byref(_read_count)
    )
    read_input_records = _input_records[:_read_count.value]

    del _keys[:]

    for input_record in read_input_records:
        event_type = input_record.EventType

        if event_type == _KEY_EVENT:
            key_event = input_record.Event.KeyEvent
            key = key_event.uChar.UnicodeChar
            if key_event.bKeyDown or key == '\x1b':
                _keys.append(key)

    handler(_keys[:])


def _set_console_mode(file: IO[Any], mode: int) -> bool:
    '''
    Set the console mode for a given file (stdout or stdin).

    Args:
        file (IO): A file like object.
        mode (int): New mode.

    Returns:
        bool: True on success, otherwise False.

    https://docs.microsoft.com/en-us/windows/console/setconsolemode
    '''

    windows_filehandle = msvcrt.get_osfhandle(file.fileno())
    success: bool = _SetConsoleMode(windows_filehandle, mode)
    return success


def _get_console_mode(file: IO[Any]) -> int:
    '''
    Get the console mode for a given file (stdout or stdin).

    Args:
        file (IO): A file-like object.

    Returns:
        int: The current console mode.

    https://docs.microsoft.com/en-us/windows/console/getconsolemode
    '''

    windows_filehandle = msvcrt.get_osfhandle(file.fileno())
    mode = DWORD()
    _GetConsoleMode(windows_filehandle, byref(mode))
    return mode.value


def enable_virtual_terminal_sequences() -> Callable[[], None]:
    '''
    Enable virtual terminal sequences.

    Returns:
        Callable[[], None]: A callable that will restore terminal to previous state.

    https://learn.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences#samples
    '''

    terminal_in = sys.stdin
    terminal_out = sys.stdout

    current_console_mode_in = _get_console_mode(terminal_in)
    current_console_mode_out = _get_console_mode(terminal_out)

    def restore() -> None:
        '''Restore console mode to previous settings.'''

        _set_console_mode(terminal_in, current_console_mode_in)
        _set_console_mode(terminal_out, current_console_mode_out)

    _set_console_mode(terminal_in, current_console_mode_in | _ENABLE_VIRTUAL_TERMINAL_INPUT)
    return restore
