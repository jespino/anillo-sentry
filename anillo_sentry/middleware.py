import functools

from anillo.http.responses import Response

from raven import Client


def wrap_sentry(func=None, *, url):
    """
    A middleware that capture exceptions and send it to the
    sentry server.

    This middleware requires a `url` keyword
    only parameter for provide the sentry url.

    :param url: Sentry url.
    :type url: dictionary
    """

    if func is None:
        return functools.partial(wrap_sentry, url=url)

    client = Client(url)

    def wrapper(request):
        try:
            return func(request)
        except Exception as e:
            client.captureException(extra={"request": request})
            raise e

    return wrapper
