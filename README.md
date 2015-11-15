# smcomm
S&amp;M Community

## Installation

make a virtualenv ;)

    pip install pelican feedparser peewee

replace the file pelicanconf.py and publishconf.py by the one provided here


create the database by entering :

    python load_data.py


update the date triggered column to be able to grab several data

    sqlite3 smcomm.db
    update feeds set date_triggered = '2014-01-01 18:00:00.0000';


grab the feeds :

    python grab_data.py


generate html file

    make html

launch the server

    make server

![voici le rendu](https://raw.githubusercontent.com/foxmask/smcomm/master/smcomm.png)
