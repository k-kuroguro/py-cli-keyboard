from enum import Enum


# Adapted from Textual https://github.com/Textualize/textual/blob/main/src/textual/keys.py.
# See ./Textual_LICENSE.


class Keys(str, Enum):
    '''
    List of keys for use in key bindings.

    Note that this is an 'StrEnum', all values can be compared against strings.
    '''

    value: str

    ESCAPE = 'escape'  # Also Control-[
    SHIFT_ESCAPE = 'shift+escape'
    RETURN = 'return'
    ENTER = 'enter'

    CONTROL_AT = 'ctrl+@'  # Also Control-Space.

    CONTROL_A = 'ctrl+a'
    CONTROL_B = 'ctrl+b'
    CONTROL_C = 'ctrl+c'
    CONTROL_D = 'ctrl+d'
    CONTROL_E = 'ctrl+e'
    CONTROL_F = 'ctrl+f'
    CONTROL_G = 'ctrl+g'
    CONTROL_H = 'ctrl+h'
    CONTROL_I = 'ctrl+i'  # Tab
    CONTROL_J = 'ctrl+j'  # Newline
    CONTROL_K = 'ctrl+k'
    CONTROL_L = 'ctrl+l'
    CONTROL_M = 'ctrl+m'  # Carriage return
    CONTROL_N = 'ctrl+n'
    CONTROL_O = 'ctrl+o'
    CONTROL_P = 'ctrl+p'
    CONTROL_Q = 'ctrl+q'
    CONTROL_R = 'ctrl+r'
    CONTROL_S = 'ctrl+s'
    CONTROL_T = 'ctrl+t'
    CONTROL_U = 'ctrl+u'
    CONTROL_V = 'ctrl+v'
    CONTROL_W = 'ctrl+w'
    CONTROL_X = 'ctrl+x'
    CONTROL_Y = 'ctrl+y'
    CONTROL_Z = 'ctrl+z'

    CONTROL_1 = 'ctrl+1'
    CONTROL_2 = 'ctrl+2'
    CONTROL_3 = 'ctrl+3'
    CONTROL_4 = 'ctrl+4'
    CONTROL_5 = 'ctrl+5'
    CONTROL_6 = 'ctrl+6'
    CONTROL_7 = 'ctrl+7'
    CONTROL_8 = 'ctrl+8'
    CONTROL_9 = 'ctrl+9'
    CONTROL_0 = 'ctrl+0'

    CONTROL_SHIFT_1 = 'ctrl+shift+1'
    CONTROL_SHIFT_2 = 'ctrl+shift+2'
    CONTROL_SHIFT_3 = 'ctrl+shift+3'
    CONTROL_SHIFT_4 = 'ctrl+shift+4'
    CONTROL_SHIFT_5 = 'ctrl+shift+5'
    CONTROL_SHIFT_6 = 'ctrl+shift+6'
    CONTROL_SHIFT_7 = 'ctrl+shift+7'
    CONTROL_SHIFT_8 = 'ctrl+shift+8'
    CONTROL_SHIFT_9 = 'ctrl+shift+9'
    CONTROL_SHIFT_0 = 'ctrl+shift+0'

    CONTROL_BACKSLASH = 'ctrl+\\'
    CONTROL_SQUARE_CLOSE = 'ctrl+]'
    CONTROL_CIRCUMFLEX = 'ctrl+^'
    CONTROL_UNDERSCORE = 'ctrl+_'

    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
    HOME = 'home'
    END = 'end'
    INSERT = 'insert'
    DELETE = 'delete'
    PAGE_UP = 'pageup'
    PAGE_DOWN = 'pagedown'

    CONTROL_LEFT = 'ctrl+left'
    CONTROL_RIGHT = 'ctrl+right'
    CONTROL_UP = 'ctrl+up'
    CONTROL_DOWN = 'ctrl+down'
    CONTROL_HOME = 'ctrl+home'
    CONTROL_END = 'ctrl+end'
    CONTROL_INSERT = 'ctrl+insert'
    CONTROL_DELETE = 'ctrl+delete'
    CONTROL_PAGE_UP = 'ctrl+pageup'
    CONTROL_PAGE_DOWN = 'ctrl+pagedown'

    SHIFT_LEFT = 'shift+left'
    SHIFT_RIGHT = 'shift+right'
    SHIFT_UP = 'shift+up'
    SHIFT_DOWN = 'shift+down'
    SHIFT_HOME = 'shift+home'
    SHIFT_END = 'shift+end'
    SHIFT_INSERT = 'shift+insert'
    SHIFT_DELETE = 'shift+delete'
    SHIFT_PAGE_UP = 'shift+pageup'
    SHIFT_PAGE_DOWN = 'shift+pagedown'

    CONTROL_SHIFT_LEFT = 'ctrl+shift+left'
    CONTROL_SHIFT_RIGHT = 'ctrl+shift+right'
    CONTROL_SHIFT_UP = 'ctrl+shift+up'
    CONTROL_SHIFT_DOWN = 'ctrl+shift+down'
    CONTROL_SHIFT_HOME = 'ctrl+shift+home'
    CONTROL_SHIFT_END = 'ctrl+shift+end'
    CONTROL_SHIFT_INSERT = 'ctrl+shift+insert'
    CONTROL_SHIFT_DELETE = 'ctrl+shift+delete'
    CONTROL_SHIFT_PAGE_UP = 'ctrl+shift+pageup'
    CONTROL_SHIFT_PAGE_DOWN = 'ctrl+shift+pagedown'

    BACK_TAB = 'shift+tab'  # shift + tab

    F1 = 'f1'
    F2 = 'f2'
    F3 = 'f3'
    F4 = 'f4'
    F5 = 'f5'
    F6 = 'f6'
    F7 = 'f7'
    F8 = 'f8'
    F9 = 'f9'
    F10 = 'f10'
    F11 = 'f11'
    F12 = 'f12'
    F13 = 'f13'
    F14 = 'f14'
    F15 = 'f15'
    F16 = 'f16'
    F17 = 'f17'
    F18 = 'f18'
    F19 = 'f19'
    F20 = 'f20'
    F21 = 'f21'
    F22 = 'f22'
    F23 = 'f23'
    F24 = 'f24'

    CONTROL_F1 = 'ctrl+f1'
    CONTROL_F2 = 'ctrl+f2'
    CONTROL_F3 = 'ctrl+f3'
    CONTROL_F4 = 'ctrl+f4'
    CONTROL_F5 = 'ctrl+f5'
    CONTROL_F6 = 'ctrl+f6'
    CONTROL_F7 = 'ctrl+f7'
    CONTROL_F8 = 'ctrl+f8'
    CONTROL_F9 = 'ctrl+f9'
    CONTROL_F10 = 'ctrl+f10'
    CONTROL_F11 = 'ctrl+f11'
    CONTROL_F12 = 'ctrl+f12'
    CONTROL_F13 = 'ctrl+f13'
    CONTROL_F14 = 'ctrl+f14'
    CONTROL_F15 = 'ctrl+f15'
    CONTROL_F16 = 'ctrl+f16'
    CONTROL_F17 = 'ctrl+f17'
    CONTROL_F18 = 'ctrl+f18'
    CONTROL_F19 = 'ctrl+f19'
    CONTROL_F20 = 'ctrl+f20'
    CONTROL_F21 = 'ctrl+f21'
    CONTROL_F22 = 'ctrl+f22'
    CONTROL_F23 = 'ctrl+f23'
    CONTROL_F24 = 'ctrl+f24'

    # Matches any key.
    ANY = '<any>'

    # Special.
    SCROLL_UP = '<scroll-up>'
    SCROLL_DOWN = '<scroll-down>'

    CPR_RESPONSE = '<cursor-position-response>'
    VT100_MOUSE_EVENT = '<vt100-mouse-event>'
    WINDOWS_MOUSE_EVENT = '<windowshift+mouse-event>'
    BRACKETED_PASTE = '<bracketed-paste>'

    # For internal use: key which is ignored.
    # (The key binding for this key should not do anything.)
    IGNORE = '<ignore>'

    # Some 'Key' aliases (for backwardshift+compatibility).
    CONTROL_SPACE = CONTROL_AT
    TAB = CONTROL_I
    BACKSPACE = CONTROL_H

    SHIFT_CONTROL_LEFT = CONTROL_SHIFT_LEFT
    SHIFT_CONTROL_RIGHT = CONTROL_SHIFT_RIGHT
    SHIFT_CONTROL_HOME = CONTROL_SHIFT_HOME
    SHIFT_CONTROL_END = CONTROL_SHIFT_END
