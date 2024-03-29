# api/server.py
from flask import Flask
from cfg import ConfigVars as conf_var

app: Flask = Flask(conf_var.service_name)


@app.route('/health')
def health():
    return 'OK', 200
