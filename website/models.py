# coding: utf-8
from peewee import *
import datetime

db = SqliteDatabase('smcomm.db', threadlocals=True)


class BaseModel(Model):
    class Meta:
        database = db


class Feeds(BaseModel):
    site_name = CharField()
    site_url = TextField()
    feed_url = TextField()
    date_triggered = DateTimeField(default=datetime.datetime.now, formats=['%Y-%m-%d %H:%M'])
    active = BooleanField(default=True)
    uuid = CharField()


# Create db if not exist
try:
    Feeds.create_table()
except Exception:
    pass
