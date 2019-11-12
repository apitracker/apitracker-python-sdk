## apitracker python sdk

This is a library to monkeypatch http.client to send request to apitracker proxy. 

apitracker is API integration reliability as a service. It provides a network proxy that lets developers adds monitoring, error alerting, auto retry and more to their API integration, all with zero code change. 

Sign up at https://apitracker.com for a free account

### Installation
apitracker-python-sdk is available on PyPI and thus can be installed with pip on most platforms.

```
$ pip install apitracker-python-sdk
```

### Getting started
This example shows how to use instantiate the library 


* Sign up for an account with apitracker
* Create an api and enter the api hostname, e.g. api.xkcd.com
* Copy the apitracker proxy hostname, e.g. xxxx.apitracker.net
* Put the following snippet of code, ideally at the top of your python program

```python
from apitracker_python_sdk import Patcher
apitracker_config = {
    '<original api hostname>': {
        'url': '<apitracker proxy host name>'
    }
}
apitracker_patcher = Patcher(apitracker_config)
apitracker_patcher.patch()
```

* To disable: 

```python
apitracker_patcher.unpatch()
```

### To do
Add more control, such as percentage of traffic to go through apitracker vs the original endpoint