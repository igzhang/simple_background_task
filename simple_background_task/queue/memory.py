"""

@author: fallenthrough
"""
from queue import Queue
from simple_background_task.queue.interface import QueueInterface
from simple_background_task.task import Task


class MemoryQueue(QueueInterface):
    """
    a memory queue implement interface for get background task
    """

    def __init__(self):
        self._queue = Queue()

    def get(self) -> Task:
        return self._queue.get()

    def put(self, to_do_task: Task) -> None:
        self._queue.put(to_do_task, block=False)
