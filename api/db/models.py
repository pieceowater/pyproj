# api/db/models.py
from peewee import Model, CharField, IntegerField, ForeignKeyField, PrimaryKeyField
from api.db import db


class User(Model):
    user_id = PrimaryKeyField()
    name = CharField()

    class Meta:
        database = db


class Post(Model):
    post_id = PrimaryKeyField()
    title = CharField()
    content = CharField()
    views = IntegerField(default=0)
    author = ForeignKeyField(User, backref='posts')

    class Meta:
        database = db
