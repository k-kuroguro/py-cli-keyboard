from .keys import Keys


# Adapted from Textual https://github.com/Textualize/textual/blob/main/src/textual/_ansi_sequences.py.
# See ./Textual_LICENSE.


# Mapping of vt100 escape codes to Keys.
# https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences
ANSI_SEQUENCES: dict[str, tuple[Keys, ...]] = {
    # Control keys.
    '\r': (Keys.ENTER,),
    '\x00': (Keys.CONTROL_AT,),  # Control-At (Also for Ctrl-Space)
    '\x01': (Keys.CONTROL_A,),  # Control-A (home)
    '\x02': (Keys.CONTROL_B,),  # Control-B (emacs cursor left)
    '\x03': (Keys.CONTROL_C,),  # Control-C (interrupt)
    '\x04': (Keys.CONTROL_D,),  # Control-D (exit)
    '\x05': (Keys.CONTROL_E,),  # Control-E (end)
    '\x06': (Keys.CONTROL_F,),  # Control-F (cursor forward)
    '\x07': (Keys.CONTROL_G,),  # Control-G
    '\x08': (Keys.CONTROL_H,),  # Control-H (8) (Identical to '\b')
    '\x09': (Keys.CONTROL_I,),  # Control-I (9) (Identical to '\t')
    '\x0a': (Keys.CONTROL_J,),  # Control-J (10) (Identical to '\n')
    '\x0b': (Keys.CONTROL_K,),  # Control-K (delete until end of line; vertical tab)
    '\x0c': (Keys.CONTROL_L,),  # Control-L (clear; form feed)
    # '\x0d': (Keys.CONTROL_M,),  # Control-M (13) (Identical to '\r')
    '\x0e': (Keys.CONTROL_N,),  # Control-N (14) (history forward)
    '\x0f': (Keys.CONTROL_O,),  # Control-O (15)
    '\x10': (Keys.CONTROL_P,),  # Control-P (16) (history back)
    '\x11': (Keys.CONTROL_Q,),  # Control-Q
    '\x12': (Keys.CONTROL_R,),  # Control-R (18) (reverse search)
    '\x13': (Keys.CONTROL_S,),  # Control-S (19) (forward search)
    '\x14': (Keys.CONTROL_T,),  # Control-T
    '\x15': (Keys.CONTROL_U,),  # Control-U
    '\x16': (Keys.CONTROL_V,),  # Control-V
    '\x17': (Keys.CONTROL_W,),  # Control-W
    '\x18': (Keys.CONTROL_X,),  # Control-X
    '\x19': (Keys.CONTROL_Y,),  # Control-Y (25)
    '\x1a': (Keys.CONTROL_Z,),  # Control-Z
    '\x1b': (Keys.ESCAPE,),  # Also Control-[
    '\x1b\x1b': (Keys.ESCAPE,),  # Windows issues esc esc for a single press of escape key
    '\x9b': (Keys.SHIFT_ESCAPE,),
    '\x1c': (Keys.CONTROL_BACKSLASH,),  # Both Control-\ (also Ctrl-| )
    '\x1d': (Keys.CONTROL_SQUARE_CLOSE,),  # Control-]
    '\x1e': (Keys.CONTROL_CIRCUMFLEX,),  # Control-^
    '\x1f': (Keys.CONTROL_UNDERSCORE,),  # Control-underscore (Also for Ctrl-hyphen.)
    # ASCII Delete (0x7f)
    # Vt220 (and Linux terminal) send this when pressing backspace. We map this
    # to ControlH, because that will make it easier to create key bindings that
    # work everywhere, with the trade-off that it's no longer possible to
    # handle backspace and control-h individually for the few terminals that
    # support it. (Most terminals send ControlH when backspace is pressed.)
    # See: http://www.ibb.net/~anne/keyboard.html
    '\x7f': (Keys.CONTROL_H,),
    # --
    # Various
    '\x1b[1~': (Keys.HOME,),  # tmux
    '\x1b[2~': (Keys.INSERT,),
    '\x1b[3~': (Keys.DELETE,),
    '\x1b[4~': (Keys.END,),  # tmux
    '\x1b[5~': (Keys.PAGE_UP,),
    '\x1b[6~': (Keys.PAGE_DOWN,),
    '\x1b[7~': (Keys.HOME,),  # xrvt
    '\x1b[8~': (Keys.END,),  # xrvt
    '\x1b[Z': (Keys.BACK_TAB,),  # shift + tab
    '\x1b\x09': (Keys.BACK_TAB,),  # Linux console
    '\x1b[~': (Keys.BACK_TAB,),  # Windows console
    # --
    # Function keys.
    '\x1bOP': (Keys.F1,),
    '\x1bOQ': (Keys.F2,),
    '\x1bOR': (Keys.F3,),
    '\x1bOS': (Keys.F4,),
    '\x1b[[A': (Keys.F1,),  # Linux console.
    '\x1b[[B': (Keys.F2,),  # Linux console.
    '\x1b[[C': (Keys.F3,),  # Linux console.
    '\x1b[[D': (Keys.F4,),  # Linux console.
    '\x1b[[E': (Keys.F5,),  # Linux console.
    '\x1b[11~': (Keys.F1,),  # rxvt-unicode
    '\x1b[12~': (Keys.F2,),  # rxvt-unicode
    '\x1b[13~': (Keys.F3,),  # rxvt-unicode
    '\x1b[14~': (Keys.F4,),  # rxvt-unicode
    '\x1b[15~': (Keys.F5,),
    '\x1b[17~': (Keys.F6,),
    '\x1b[18~': (Keys.F7,),
    '\x1b[19~': (Keys.F8,),
    '\x1b[20~': (Keys.F9,),
    '\x1b[21~': (Keys.F10,),
    '\x1b[23~': (Keys.F11,),
    '\x1b[24~': (Keys.F12,),
    '\x1b[25~': (Keys.F13,),
    '\x1b[26~': (Keys.F14,),
    '\x1b[28~': (Keys.F15,),
    '\x1b[29~': (Keys.F16,),
    '\x1b[31~': (Keys.F17,),
    '\x1b[32~': (Keys.F18,),
    '\x1b[33~': (Keys.F19,),
    '\x1b[34~': (Keys.F20,),
    # Xterm
    '\x1b[1;2P': (Keys.F13,),
    '\x1b[1;2Q': (Keys.F14,),
    # '\x1b[1;2R': (Keys.F15,),  # Conflicts with CPR response.
    '\x1b[1;2S': (Keys.F16,),
    '\x1b[15;2~': (Keys.F17,),
    '\x1b[17;2~': (Keys.F18,),
    '\x1b[18;2~': (Keys.F19,),
    '\x1b[19;2~': (Keys.F20,),
    '\x1b[20;2~': (Keys.F21,),
    '\x1b[21;2~': (Keys.F22,),
    '\x1b[23;2~': (Keys.F23,),
    '\x1b[24;2~': (Keys.F24,),
    # --
    # Control + function keys.
    '\x1b[1;5P': (Keys.CONTROL_F1,),
    '\x1b[1;5Q': (Keys.CONTROL_F2,),
    # '\x1b[1;5R': (Keys.CONTROL_F3,),  # Conflicts with CPR response.
    '\x1b[1;5S': (Keys.CONTROL_F4,),
    '\x1b[15;5~': (Keys.CONTROL_F5,),
    '\x1b[17;5~': (Keys.CONTROL_F6,),
    '\x1b[18;5~': (Keys.CONTROL_F7,),
    '\x1b[19;5~': (Keys.CONTROL_F8,),
    '\x1b[20;5~': (Keys.CONTROL_F9,),
    '\x1b[21;5~': (Keys.CONTROL_F10,),
    '\x1b[23;5~': (Keys.CONTROL_F11,),
    '\x1b[24;5~': (Keys.CONTROL_F12,),
    '\x1b[1;6P': (Keys.CONTROL_F13,),
    '\x1b[1;6Q': (Keys.CONTROL_F14,),
    # '\x1b[1;6R': (Keys.CONTROL_F15,),  # Conflicts with CPR response.
    '\x1b[1;6S': (Keys.CONTROL_F16,),
    '\x1b[15;6~': (Keys.CONTROL_F17,),
    '\x1b[17;6~': (Keys.CONTROL_F18,),
    '\x1b[18;6~': (Keys.CONTROL_F19,),
    '\x1b[19;6~': (Keys.CONTROL_F20,),
    '\x1b[20;6~': (Keys.CONTROL_F21,),
    '\x1b[21;6~': (Keys.CONTROL_F22,),
    '\x1b[23;6~': (Keys.CONTROL_F23,),
    '\x1b[24;6~': (Keys.CONTROL_F24,),
    # --
    # Tmux (Win32 subsystem) sends the following scroll events.
    '\x1b[62~': (Keys.SCROLL_UP,),
    '\x1b[63~': (Keys.SCROLL_DOWN,),
    '\x1b[200~': (Keys.BRACKETED_PASTE,),  # Start of bracketed paste.
    # --
    # Sequences generated by numpad 5. Not sure what it means. (It doesn't
    # appear in 'infocmp'. Just ignore.
    '\x1b[E': (Keys.IGNORE,),  # Xterm.
    '\x1b[G': (Keys.IGNORE,),  # Linux console.
    # --
    # Meta/control/escape + pageup/pagedown/insert/delete.
    '\x1b[3;2~': (Keys.SHIFT_DELETE,),  # xterm, gnome-terminal.
    '\x1b[5;2~': (Keys.SHIFT_PAGE_UP,),
    '\x1b[6;2~': (Keys.SHIFT_PAGE_DOWN,),
    '\x1b[2;3~': (Keys.ESCAPE, Keys.INSERT,),
    '\x1b[3;3~': (Keys.ESCAPE, Keys.DELETE,),
    '\x1b[5;3~': (Keys.ESCAPE, Keys.PAGE_UP,),
    '\x1b[6;3~': (Keys.ESCAPE, Keys.PAGE_DOWN,),
    '\x1b[2;4~': (Keys.ESCAPE, Keys.SHIFT_INSERT,),
    '\x1b[3;4~': (Keys.ESCAPE, Keys.SHIFT_DELETE,),
    '\x1b[5;4~': (Keys.ESCAPE, Keys.SHIFT_PAGE_UP,),
    '\x1b[6;4~': (Keys.ESCAPE, Keys.SHIFT_PAGE_DOWN,),
    '\x1b[3;5~': (Keys.CONTROL_DELETE,),  # xterm, gnome-terminal.
    '\x1b[5;5~': (Keys.CONTROL_PAGE_UP,),
    '\x1b[6;5~': (Keys.CONTROL_PAGE_DOWN,),
    '\x1b[3;6~': (Keys.CONTROL_SHIFT_DELETE,),
    '\x1b[5;6~': (Keys.CONTROL_SHIFT_PAGE_UP,),
    '\x1b[6;6~': (Keys.CONTROL_SHIFT_PAGE_DOWN,),
    '\x1b[2;7~': (Keys.ESCAPE, Keys.CONTROL_INSERT,),
    '\x1b[5;7~': (Keys.ESCAPE, Keys.CONTROL_PAGE_DOWN,),
    '\x1b[6;7~': (Keys.ESCAPE, Keys.CONTROL_PAGE_DOWN,),
    '\x1b[2;8~': (Keys.ESCAPE, Keys.CONTROL_SHIFT_INSERT,),
    '\x1b[5;8~': (Keys.ESCAPE, Keys.CONTROL_SHIFT_PAGE_DOWN,),
    '\x1b[6;8~': (Keys.ESCAPE, Keys.CONTROL_SHIFT_PAGE_DOWN,),
    # --
    # Arrows.
    # (Normal cursor mode).
    '\x1b[A': (Keys.UP,),
    '\x1b[B': (Keys.DOWN,),
    '\x1b[C': (Keys.RIGHT,),
    '\x1b[D': (Keys.LEFT,),
    '\x1b[H': (Keys.HOME,),
    '\x1b[F': (Keys.END,),
    # Tmux sends following keystrokes when control+arrow is pressed, but for
    # Emacs ansi-term sends the same sequences for normal arrow keys. Consider
    # it a normal arrow press, because that's more important.
    # (Application cursor mode).
    '\x1bOA': (Keys.UP,),
    '\x1bOB': (Keys.DOWN,),
    '\x1bOC': (Keys.RIGHT,),
    '\x1bOD': (Keys.LEFT,),
    '\x1bOF': (Keys.END,),
    '\x1bOH': (Keys.HOME,),
    # Shift + arrows.
    '\x1b[1;2A': (Keys.SHIFT_UP,),
    '\x1b[1;2B': (Keys.SHIFT_DOWN,),
    '\x1b[1;2C': (Keys.SHIFT_RIGHT,),
    '\x1b[1;2D': (Keys.SHIFT_LEFT,),
    '\x1b[1;2F': (Keys.SHIFT_END,),
    '\x1b[1;2H': (Keys.SHIFT_HOME,),
    # Meta + arrow keys. Several terminals handle this differently.
    # The following sequences are for xterm and gnome-terminal.
    #     (Iterm sends ESC followed by the normal arrow_up/down/left/right
    #     sequences, and the OSX Terminal sends ESCb and ESCf for 'alt
    #     arrow_left' and 'alt arrow_right.' We don't handle these
    #     explicitly, in here, because would could not distinguish between
    #     pressing ESC (to go to Vi navigation mode), followed by just the
    #     'b' or 'f' key. These combinations are handled in
    #     the input processor.)
    '\x1b[1;3A': (Keys.ESCAPE, Keys.UP,),
    '\x1b[1;3B': (Keys.ESCAPE, Keys.DOWN,),
    '\x1b[1;3C': (Keys.ESCAPE, Keys.RIGHT,),
    '\x1b[1;3D': (Keys.ESCAPE, Keys.LEFT,),
    '\x1b[1;3F': (Keys.ESCAPE, Keys.END,),
    '\x1b[1;3H': (Keys.ESCAPE, Keys.HOME,),
    # Alt+shift+number.
    '\x1b[1;4A': (Keys.ESCAPE, Keys.SHIFT_DOWN,),
    '\x1b[1;4B': (Keys.ESCAPE, Keys.SHIFT_UP,),
    '\x1b[1;4C': (Keys.ESCAPE, Keys.SHIFT_RIGHT,),
    '\x1b[1;4D': (Keys.ESCAPE, Keys.SHIFT_LEFT,),
    '\x1b[1;4F': (Keys.ESCAPE, Keys.SHIFT_END,),
    '\x1b[1;4H': (Keys.ESCAPE, Keys.SHIFT_HOME,),
    # Control + arrows.
    '\x1b[1;5A': (Keys.CONTROL_UP,),  # Cursor Mode
    '\x1b[1;5B': (Keys.CONTROL_DOWN,),  # Cursor Mode
    '\x1b[1;5C': (Keys.CONTROL_RIGHT,),  # Cursor Mode
    '\x1b[1;5D': (Keys.CONTROL_LEFT,),  # Cursor Mode
    '\x1b[1;5F': (Keys.CONTROL_END,),
    '\x1b[1;5H': (Keys.CONTROL_HOME,),
    # Tmux sends following keystrokes when control+arrow is pressed, but for
    # Emacs ansi-term sends the same sequences for normal arrow keys. Consider
    # it a normal arrow press, because that's more important.
    '\x1b[5A': (Keys.CONTROL_UP,),
    '\x1b[5B': (Keys.CONTROL_DOWN,),
    '\x1b[5C': (Keys.CONTROL_RIGHT,),
    '\x1b[5D': (Keys.CONTROL_LEFT,),
    '\x1bOc': (Keys.CONTROL_RIGHT,),  # rxvt
    '\x1bOd': (Keys.CONTROL_LEFT,),  # rxvt
    # Control + shift + arrows.
    '\x1b[1;6A': (Keys.CONTROL_SHIFT_DOWN,),
    '\x1b[1;6B': (Keys.CONTROL_SHIFT_UP,),
    '\x1b[1;6C': (Keys.CONTROL_SHIFT_RIGHT,),
    '\x1b[1;6D': (Keys.CONTROL_SHIFT_LEFT,),
    '\x1b[1;6F': (Keys.CONTROL_SHIFT_END,),
    '\x1b[1;6H': (Keys.CONTROL_SHIFT_HOME,),
    # Control + Meta + arrows.
    '\x1b[1;7A': (Keys.ESCAPE, Keys.CONTROL_DOWN,),
    '\x1b[1;7B': (Keys.ESCAPE, Keys.CONTROL_UP,),
    '\x1b[1;7C': (Keys.ESCAPE, Keys.CONTROL_RIGHT,),
    '\x1b[1;7D': (Keys.ESCAPE, Keys.CONTROL_LEFT,),
    '\x1b[1;7F': (Keys.ESCAPE, Keys.CONTROL_END,),
    '\x1b[1;7H': (Keys.ESCAPE, Keys.CONTROL_HOME,),
    # Meta + Shift + arrows.
    '\x1b[1;8A': (Keys.ESCAPE, Keys.CONTROL_SHIFT_DOWN,),
    '\x1b[1;8B': (Keys.ESCAPE, Keys.CONTROL_SHIFT_UP,),
    '\x1b[1;8C': (Keys.ESCAPE, Keys.CONTROL_SHIFT_RIGHT,),
    '\x1b[1;8D': (Keys.ESCAPE, Keys.CONTROL_SHIFT_LEFT,),
    '\x1b[1;8F': (Keys.ESCAPE, Keys.CONTROL_SHIFT_END,),
    '\x1b[1;8H': (Keys.ESCAPE, Keys.CONTROL_SHIFT_HOME,),
    # Meta + arrow on (some?) Macs when using iTerm defaults (see issue #483).
    '\x1b[1;9A': (Keys.ESCAPE, Keys.UP,),
    '\x1b[1;9B': (Keys.ESCAPE, Keys.DOWN,),
    '\x1b[1;9C': (Keys.ESCAPE, Keys.RIGHT,),
    '\x1b[1;9D': (Keys.ESCAPE, Keys.LEFT,),
    # --
    # Control/shift/meta + number in mintty.
    # (c-2 will actually send c-@ and c-6 will send c-^.)
    '\x1b[1;5p': (Keys.CONTROL_0,),
    '\x1b[1;5q': (Keys.CONTROL_1,),
    '\x1b[1;5r': (Keys.CONTROL_2,),
    '\x1b[1;5s': (Keys.CONTROL_3,),
    '\x1b[1;5t': (Keys.CONTROL_4,),
    '\x1b[1;5u': (Keys.CONTROL_5,),
    '\x1b[1;5v': (Keys.CONTROL_6,),
    '\x1b[1;5w': (Keys.CONTROL_7,),
    '\x1b[1;5x': (Keys.CONTROL_8,),
    '\x1b[1;5y': (Keys.CONTROL_9,),
    '\x1b[1;6p': (Keys.CONTROL_SHIFT_0,),
    '\x1b[1;6q': (Keys.CONTROL_SHIFT_1,),
    '\x1b[1;6r': (Keys.CONTROL_SHIFT_2,),
    '\x1b[1;6s': (Keys.CONTROL_SHIFT_3,),
    '\x1b[1;6t': (Keys.CONTROL_SHIFT_4,),
    '\x1b[1;6u': (Keys.CONTROL_SHIFT_5,),
    '\x1b[1;6v': (Keys.CONTROL_SHIFT_6,),
    '\x1b[1;6w': (Keys.CONTROL_SHIFT_7,),
    '\x1b[1;6x': (Keys.CONTROL_SHIFT_8,),
    '\x1b[1;6y': (Keys.CONTROL_SHIFT_9,),
    '\x1b[1;7p': (Keys.ESCAPE, Keys.CONTROL_0,),
    '\x1b[1;7q': (Keys.ESCAPE, Keys.CONTROL_1,),
    '\x1b[1;7r': (Keys.ESCAPE, Keys.CONTROL_2,),
    '\x1b[1;7s': (Keys.ESCAPE, Keys.CONTROL_3,),
    '\x1b[1;7t': (Keys.ESCAPE, Keys.CONTROL_4,),
    '\x1b[1;7u': (Keys.ESCAPE, Keys.CONTROL_5,),
    '\x1b[1;7v': (Keys.ESCAPE, Keys.CONTROL_6,),
    '\x1b[1;7w': (Keys.ESCAPE, Keys.CONTROL_7,),
    '\x1b[1;7x': (Keys.ESCAPE, Keys.CONTROL_8,),
    '\x1b[1;7y': (Keys.ESCAPE, Keys.CONTROL_9,),
    '\x1b[1;8p': (Keys.ESCAPE, Keys.CONTROL_SHIFT_0,),
    '\x1b[1;8q': (Keys.ESCAPE, Keys.CONTROL_SHIFT_1,),
    '\x1b[1;8r': (Keys.ESCAPE, Keys.CONTROL_SHIFT_2,),
    '\x1b[1;8s': (Keys.ESCAPE, Keys.CONTROL_SHIFT_3,),
    '\x1b[1;8t': (Keys.ESCAPE, Keys.CONTROL_SHIFT_4,),
    '\x1b[1;8u': (Keys.ESCAPE, Keys.CONTROL_SHIFT_5,),
    '\x1b[1;8v': (Keys.ESCAPE, Keys.CONTROL_SHIFT_6,),
    '\x1b[1;8w': (Keys.ESCAPE, Keys.CONTROL_SHIFT_7,),
    '\x1b[1;8x': (Keys.ESCAPE, Keys.CONTROL_SHIFT_8,),
    '\x1b[1;8y': (Keys.ESCAPE, Keys.CONTROL_SHIFT_9,)
}
