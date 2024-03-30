# api/tools/token_gen.py
from cfg import ConfigVars as conf_var
import jwt
import datetime


def get_token(identity, ttl_min=30, algorithm="HS256"):
    return jwt.encode(
        {
            'identity': identity,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=ttl_min)
        },
        conf_var.secret_key,
        algorithm=algorithm
    )
