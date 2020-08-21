"""

@author: fallenthrough
"""
from abc import ABCMeta, abstractmethod
from simple_background_task.task import Task


class QueueInterface(metaclass=ABCMeta):
    """
    an queue interface for get background task
    """

    @abstractmethod
    def get(self) -> Task:
        """
        get task block

        :return:
        """

    @abstractmethod
    def put(self, to_do_task: Task) -> None:
        """
        put a background task

        :return:
        """
