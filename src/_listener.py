import atexit
import platform
from queue import Queue
from threading import Event, Lock, Thread
from typing import Callable, Optional

from .event import KeyEvent
from ._parser import Parser


if platform.system() == 'Windows':
    from ._windows import listen, enable_virtual_terminal_sequences
    _restore = enable_virtual_terminal_sequences()
    atexit.register(_restore)
else:
    raise NotImplementedError()


Handler = Callable[[KeyEvent], None]


class Listener:

    def __init__(self) -> None:
        self._running: bool = False
        self._handlers: list[Handler] = []
        self._queue: Queue[KeyEvent] = Queue()
        self._lock = Lock()
        self._stop_event = Event()
        self._listening_thread: Optional[Thread] = None
        self._processing_thread: Optional[Thread] = None

    def start(self) -> None:
        '''Start listener if it hasn't started.'''

        with self._lock:
            if self._running:
                return

            self._running = True
            self._stop_event.clear()

            self._listening_thread = Thread(target=self._listen)
            self._listening_thread.daemon = True
            self._listening_thread.start()

            self._processing_thread = Thread(target=self._process)
            self._processing_thread.daemon = True
            self._processing_thread.start()

    def stop(self) -> None:
        '''Stop running listener.'''

        with self._lock:
            if not self._running:
                return

            self._running = False
            self._stop_event.set()

            if self._listening_thread is not None:
                self._listening_thread.join()
            if self._processing_thread is not None:
                self._processing_thread.join()

            self._listening_thread = None
            self._processing_thread = None

    def add_handler(self, handler: Handler) -> None:
        with self._lock:
            self._handlers.append(handler)

    def remove_handler(self, handler: Handler) -> None:
        '''Remove all handlers from list.'''

        with self._lock:
            while handler in self._handlers:
                self._handlers.remove(handler)

    def _listen(self) -> None:
        parser = Parser()

        def put_queue(keys: list[str]) -> None:
            for event in parser.parse(''.join(keys)):
                self._queue.put(event)

        while not self._stop_requested():
            listen(put_queue)

    def _process(self) -> None:
        while not self._stop_requested():
            event = self._queue.get()
            self._invoke_handlers(event)
            self._queue.task_done()

    def _invoke_handlers(self, event: KeyEvent) -> None:
        with self._lock:
            for handler in self._handlers:
                handler(event)

    def _stop_requested(self) -> bool:
        return self._stop_event.is_set()
