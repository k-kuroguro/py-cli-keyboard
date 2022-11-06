from typing import Generator

from .event import KeyEvent
from ._ansi_sequences import ANSI_SEQUENCES


_ESC = '\x1b'
_get_ansi_sequence = ANSI_SEQUENCES.get


class Parser():

    def parse(self, data: str) -> Generator[KeyEvent, None, None]:

        pos = 0
        data_size = len(data)

        def read1() -> str:
            nonlocal pos
            character = data[pos]
            pos += 1
            return character

        while pos < data_size:
            character = read1()

            if character == _ESC and pos != data_size:
                sequence: str = character
                while True:
                    sequence += read1()
                    keys = _get_ansi_sequence(sequence, None)
                    if keys is not None:
                        for key in keys:
                            yield KeyEvent(key=key)
                        break
            else:
                keys = _get_ansi_sequence(character, None)
                if keys is not None:
                    for key in keys:
                        yield KeyEvent(key=key)
                else:
                    yield KeyEvent(key=character)
