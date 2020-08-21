"""
@description: user api
@author: fallenthrough
"""
import threading
import logging
import traceback
from concurrent.futures import ThreadPoolExecutor
from simple_background_task.queue.interface import QueueInterface
from simple_background_task.queue.memory import MemoryQueue
from simple_background_task.task import Task


LOGGER = logging.getLogger("background_task")


class BackgroundTask(threading.Thread):
    """
    executor
    """

    QUEUE_SUPPORT_STORE = {
        "memory": MemoryQueue(),
    }
    _instance = None
    _running = True

    def __init__(self, store: str = "memory", workers: int = 3, *args, **kwargs):
        self._store = store
        self._thread_pool = ThreadPoolExecutor(workers)
        self._queue = self.choose_queue_backend_factory()
        super().__init__(*args, **kwargs)

    def choose_queue_backend_factory(self) -> QueueInterface:
        store_backend = self.QUEUE_SUPPORT_STORE.get(self._store)
        if store_backend is None:
            raise ValueError(f"{self._store} store is not support now!")
        return store_backend

    def run(self):
        while self._running:
            to_do_task = self._queue.get()
            LOGGER.info("get background task:%s", to_do_task)
            try:
                to_do_task.run()
            except Exception:
                LOGGER.error(traceback.format_exc())
            else:
                LOGGER.info("finished background task:%s", to_do_task)

    def __new__(cls, store: str = "memory", workers: int = 3, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def put(self, to_do_task: Task):
        self._queue.put(to_do_task)

    def stop(self):
        self._running = False


def defer(func, arguments: dict):
    to_do_task = Task(func, *arguments.get("args", []), **arguments.get("kwargs", {}))
    BackgroundTask().put(to_do_task)


if __name__ == '__main__':
    BackgroundTask().start()
