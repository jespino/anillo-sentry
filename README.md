# Anillo-Sentry middleware

[![Build Status](http://img.shields.io/travis/jespino/anillo-sentry.svg?branch=master)](https://travis-ci.org/jespino/anillo-sentry)
[![Coveralls Status](http://img.shields.io/coveralls/jespino/anillo-sentry/master.svg)](https://coveralls.io/r/jespino/anillo-sentry)
[![Development Status](https://pypip.in/status/anillo-sentry/badge.svg)](https://pypi.python.org/pypi/anillo-sentry/)
[![Latest Version](https://pypip.in/version/anillo-sentry/badge.svg)](https://pypi.python.org/pypi/anillo-sentry/)
[![Supported Python versions](https://pypip.in/py_versions/anillo-sentry/badge.svg)](https://pypi.python.org/pypi/anillo-sentry/)
[![License](https://pypip.in/license/anillo-sentry/badge.svg)](https://pypi.python.org/pypi/anillo-sentry/)
[![Downloads](https://pypip.in/download/anillo-sentry/badge.svg)](https://pypi.python.org/pypi/anillo-sentry/)

Anillo sentry is a middleware for sentry integration with anillo nanoframework.

## Usage

### Basic example

```python
from anillo.app import application
from anillo.handlers.routing import router, url
from anillo.middlewares.cookies import wrap_cookies
from anillo.middlewares.session import wrap_session, MemoryStorage
from anillo.http import Ok
from anillo.utils.common import chain

from anillo_sentry.middleware import wrap_sentry

import json


def index(request):
    return Ok(json.dumps(request.get('session', {}).get('identity')))


def login(request):
    request.session['identity'] = {"user_id": 1}
    raise Exception("Example error")


urls = [
    url("/", index),
    url("/login", login),
]

app = application(chain(
    wrap_sentry("http://******@localhost:8080/1"),
    wrap_cookies,
    wrap_session(storage=MemoryStorage),
    router(urls)
))

if __name__ == '__main__':
    from anillo import serving
    serving.run_simple(app, port=5000)
```
