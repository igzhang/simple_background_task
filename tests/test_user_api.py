"""
@description: test case
@author: fallenthrough
"""
import time
import pytest
from unittest.mock import MagicMock
from simple_background_task import BackgroundTask, defer
from simple_background_task.queue.memory import MemoryQueue


def test_choose_queue_backend_factory():
    task = BackgroundTask(store="memory")
    assert isinstance(task._queue, MemoryQueue)


def test_choose_not_support_queue_backend_factory():
    with pytest.raises(ValueError):
        BackgroundTask(store="ewqe")


def test_singleton():
    a1 = BackgroundTask(store="memory")
    a2 = BackgroundTask(store="memory")
    assert a1 is a2


def test_run():
    mock = MagicMock()
    obj = BackgroundTask(store="memory")
    obj.start()
    defer(
        func=mock.method,
        arguments={
            "args": [1, 2],
            "kwargs": {
                "a": "b",
            }
        }
    )
    time.sleep(1)
    obj.stop()
    mock.method.assert_called_once_with(1, 2, a="b")
