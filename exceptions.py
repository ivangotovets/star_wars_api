from requests.exceptions import RequestException


class ConnectionError(RequestException):
    pass
