# api/tools/middleware.py
from flask import request, jsonify
from cfg import ConfigVars as conf_var
from functools import wraps
import jwt


def token_required(ignore=False, algorithms="HS256"):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not ignore:
                token = request.args.get('token')

                if not token:
                    return {
                        "data": {},
                        "status": 403,
                        "message": 'Token is missing'
                    }, 403

                try:
                    data = jwt.decode(token, conf_var.secret_key, algorithms=algorithms)
                    print("Decoded token data:", data)

                except jwt.ExpiredSignatureError:
                    return {
                        "data": {},
                        "status": 403,
                        "message": 'Token has expired'
                    }, 403
                except jwt.InvalidTokenError:
                    return {
                        "data": {},
                        "status": 403,
                        "message": 'Token is invalid'
                    }, 403

            return f(*args, **kwargs)

        return decorated

    return decorator
