# coding: utf-8
from models import Feeds
import uuid
import json
from datetime import datetime


def set_uuid():
    return str(uuid.uuid4())


def feeds_to_track():
    with open('smcomm.json') as feeds:
        for line in feeds:
            data = json.loads(line)
            print("Importing data {}".format(data))
            Feeds.create(site_name=data['site_name'],
                         site_url=data['site_url'],
                         feed_url=data['feed_url'],
                         date_triggered=datetime.now(tz=None),
                         active=True,
                         uuid=set_uuid())

if __name__ == '__main__':
    feeds_to_track()
