class Event:
    __slots__ = ()


class KeyEvent(Event):
    '''Event with key press.'''

    __slots__ = ('_key',)

    def __init__(self, key: str) -> None:
        self._key: str = key

    @property
    def key(self) -> str:
        return self._key
