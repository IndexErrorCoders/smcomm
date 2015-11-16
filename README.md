# S&M Community

## Main Idea

Sharing his ressources with each others, in your own community, on a dedicated central point

## Why this application ?

The goal of this app is to provide a central point from where you can federate all the news and feeds of your community instead of having to open several times (some tools) to follow each news and feeds.

## How does it work ?

A script will grab the sources of your community and will generate articles with the help of pelican.

## Installation

make a virtualenv ;)

    pip install pelican feedparser peewee

replace the file pelicanconf.py and publishconf.py by the one provided here


create the database by entering :

    python load_data.py


for the first execution, to cheat ;) update the date triggered column to be able to grab several data

    sqlite3 smcomm.db
    update feeds set date_triggered = '2014-01-01 18:00:00.0000';


grab the feeds :

    python grab_data.py


generate html file

    make html

launch the server

    make server

the result may look like this

![voici le rendu](https://raw.githubusercontent.com/foxmask/smcomm/master/smcomm.png)
