# simple_background_task  

## Features  
- execute background task,with thread
- support multiple queue,eg memory/rocketmq(todo)
- easy to integrate with frameworks

## Install
```shell script
pip install simple_background_task
```

## Usage
```python
# start main process
from simple_background_task import BackgroundTask

BackgroundTask().start()

# start a background task
from simple_background_task import defer

def test_job():
    pass

defer(
    func=test_job,
    arguments={
        "args": [1, 2],
        "kwargs": {"a": "b"}
    }
)
```

## Test
```shell script
python -m pytest tests
```
