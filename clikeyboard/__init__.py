from typing import Callable

from ._listener import Handler, Listener
from .keys import Keys
from .event import KeyEvent


_listener = Listener()


def on_press(key: str, handler: Handler) -> Callable[[], None]:
    '''
    Invoke handler when pressed key.

    Args:
        key (str): String indicating key.
        handler (Handler): Handler to invoke.

    Returns:
        Callable[[], None]: A callable for removing handler.
    '''

    _listener.start()

    handler_checking_key: Handler = lambda event: (
        key in [Keys.ANY, event.key] or None) and handler(event)
    _listener.add_handler(handler_checking_key)

    def remove() -> None:
        _listener.remove_handler(handler_checking_key)

    return remove
