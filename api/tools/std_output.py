# api/tools/std_output.py
from functools import wraps
from flask import jsonify
from enum import Enum

from api.tools import token_required


class HTTPStatus(Enum):
    OK = 200, "OK"
    CREATED = 201, "Created"
    ACCEPTED = 202, "Accepted"
    NO_CONTENT = 204, "No Content"
    MOVED_PERMANENTLY = 301, "Moved Permanently"
    FOUND = 302, "Found"
    SEE_OTHER = 303, "See Other"
    NOT_MODIFIED = 304, "Not Modified"
    TEMPORARY_REDIRECT = 307, "Temporary Redirect"
    PERMANENT_REDIRECT = 308, "Permanent Redirect"
    BAD_REQUEST = 400, "Bad Request"
    UNAUTHORIZED = 401, "Unauthorized"
    FORBIDDEN = 403, "Forbidden"
    NOT_FOUND = 404, "Not Found"
    METHOD_NOT_ALLOWED = 405, "Method Not Allowed"
    INTERNAL_SERVER_ERROR = 500, "Internal Server Error"
    NOT_IMPLEMENTED = 501, "Not Implemented"
    BAD_GATEWAY = 502, "Bad Gateway"
    SERVICE_UNAVAILABLE = 503, "Service Unavailable"
    GATEWAY_TIMEOUT = 504, "Gateway Timeout"

    def __new__(cls, code, description):
        obj = object.__new__(cls)
        obj._value_ = code
        obj.description = description
        return obj

    def __str__(self):
        return self.description


def std_output(f=None, unprotected=False):
    if f is None:
        return lambda func: std_output(func, unprotected=unprotected)

    @wraps(f)
    @token_required(ignore=unprotected)
    def decorated(*args, **kwargs):
        data, status = f(*args, **kwargs)

        if status is None:
            status = HTTPStatus.OK.value

        message = HTTPStatus(status).description

        response = {
            "data": data,
            "status": status,
            "message": message
        }

        return jsonify(response), status

    return decorated
