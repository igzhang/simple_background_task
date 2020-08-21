"""
@description: task for execute
@author: fallenthrough
"""


class Task:
    """
    task for execute
    """

    def __init__(self, func, *args, **kwargs):
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def run(self):
        """
        run backend task

        :return:
        """
        self._func(*self._args, **self._kwargs)

    def __repr__(self):
        return "{} {} {}".format(self._func, self._args, self._kwargs)
