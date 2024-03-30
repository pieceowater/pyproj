# api/server.py
from flask import Flask
from cfg import ConfigVars as conf_var

from .db import db, models

app: Flask = Flask(conf_var.service_name)

db.connect()

# db.drop_tables([models.User, models.Post])
db.create_tables([models.User, models.Post])


@app.route('/health')
def health():
    return 'OK', 200
