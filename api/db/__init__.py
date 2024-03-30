# api/db/__init__.py
from peewee import PostgresqlDatabase
from cfg import ConfigVars as conf


db = PostgresqlDatabase(conf.db_conn_str)
