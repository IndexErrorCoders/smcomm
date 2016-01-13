# coding: utf-8
from datetime import datetime
import arrow
import time

import feedparser
from slugify import slugify

from models import Feeds

# import the configuration
from pelicanconf import *


def get_published(data):
    published = datetime.strptime('1969-01-14 18:00:00.0000', '%Y-%m-%d %H:%M:%S.%f')
    if hasattr(data, 'published_parsed'):
        published = datetime.utcfromtimestamp(
            time.mktime(data.published_parsed))
    elif hasattr(feeds, 'updated_parsed'):
        published = datetime.utcfromtimestamp(
            time.mktime(data.updated_parsed))
    return published


def to_publish(data, date_triggered):
    published = get_published(data)
    if published >= date_triggered:
        return True
    return False


def get_data(url):
    """
        read the Feed we provided in the config file
    """
    data = feedparser.parse(url, agent=FEEDS_USER_AGENT)
    return data.entries


def get_header(feed_name, data):
    """
        the header
    """
    # find one of the date  "published" or "updated"
    published = get_published(data)
    slug_published = slugify(arrow.get(published).format('YYYY-MM-DD HH:mm'))
    slug_title = slugify(data.title)

    header = '\n\t\t<meta name="date" content="{}" />\n'.format(published)
    header += '\t\t<meta name="category" content="{}" />\n'.format(feed_name)
    header += '\t\t<meta name="authors" content="{}" />\n'.format(AUTHOR)
    header += '\t\t<meta name="slug" content="{}"/>\n'.format(slug_published + '-' + slug_title)
    header += '\t</head>'

    return header


def get_title(title):
    """
        the title of the Article
    """
    return "\t<head>\n\t\t<title>{}</title>".format(title)


def get_content(data):
    """
        the body of the article
    """
    content = ''
    # check if in content or description
    if hasattr(data, 'content'):
        content = data.content[0].value
    elif hasattr(data, 'description'):
        content = data.description

    if hasattr(data, 'link'):
        content += '<p><a href="{0}">aller à la source</a></p>'.format(
            data.link)

    return "\n\t<body>{}".format(content)


def get_footer(line):
    """
        Footer of the article
        that displays what website provided
        the article
    """
    provided = "\t\t<p><em><a href='{}'>Provided by {}</a></em></p>\n\t</body>"
    return provided.format(line.site_url, line.site_name)


def get_beginpage():
    """
       start the html page
    """
    return "<html>\n"


def get_endpage():
    """
       close the html page
    """
    return "\n</html>"


def create_articles():
    """
        create one article (a file in fact) for each
        feed we get
    """
    my_date = datetime.strftime(datetime.now(), '%Y%m%d')
    my_hour = datetime.strftime(datetime.now(), '%H%M')

    for feed in Feeds.select().where(Feeds.active == True):

        # Set the date if we never grab the data before
        # date_triggered = datetime.strpftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        date_triggered = datetime.now(tz=None)
        # if feed has aleady been read before get its date
        if feed.date_triggered != '':
            # date_triggered = arrow.get(str(feed.date_triggered), 'YYYY-MM-DD HH:mm:ss')
            date_triggered = datetime.strptime(feed.date_triggered, '%Y-%m-%d %H:%M:%S.%f')

        # get the data from the feed and get them only if the date triggered >= of the feed date
        for data in get_data(feed.feed_url):

            if to_publish(data, date_triggered):

                # set the name of the file
                feed_name = feed.site_name.replace('&', 'Et').replace(' ', '_')
                # set the path of the folder where to store the article
                feed_folder = FEEDS_FOLDER + feed_name
                # cleaning the special char
                title = data.title.replace('/', '_').replace('\\', '_').replace(' ', '_').replace(':', '_').replace('&', '').replace('?', '').replace('!', '')
                filename = "{}/{}.html".format(feed_folder, title)
                print("processing {}".format(title))
                title = get_title(data.title)
                header = get_header(feed.site_name, data)
                content = get_content(data)
                footer = get_footer(feed)
                try:
                    with open(filename, 'w') as f:
                        f.write(get_beginpage())
                        f.write(title)
                        f.write(header)
                        f.write(content)
                        f.write(footer)
                        f.write(get_endpage())
                    # update the date of the trigger at each creation of article file
                    # thus, if an error occurs, we could launch the script again
                    # and start where we failed and avoid duplicate creation of article
                    feed.date_triggered = datetime.now(tz=None)
                    feed.save()

                except Exception as e:
                    raise e


if __name__ == '__main__':
    create_articles()
