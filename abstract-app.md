---
description: Build micro services with a common base Flask app.  Enforce views and routing.
---

# Abstract App

```python
from flask import Flask

import abc


class MyAbstract(Flask, abc.ABC):
    def __init__(self, *args, **kwargs):
        super(MyAbstract, self).__init__(*args, *kwargs)
        self.add_url_rule('/hello/<name>', view_func=self.hello)

    @abc.abstractmethod
    def hello(self, name):
        pass


class OtherApp(MyAbstract):
    def hello(self, name):
        return 'hi %s' % name

app = OtherApp(__name__)

app.run()
```

