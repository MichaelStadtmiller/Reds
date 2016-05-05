import time
import sqlite3
import urllib2
from xml.dom import minidom
import xml.etree.ElementTree as ET


def main():
    # create URL from mlb site
    # http://gd2.mlb.com/components/game/mlb/year_2016/month_06/day_30/epg.xml
    # https://docs.python.org/2/library/xml.etree.elementtree.html

    # gather variables
    today = time.strftime("%Y-%m-%d")
    year = time.strftime("%Y")
    month = time.strftime("%m")
    day = time.strftime("%d")

    # get reds data from the database (date, wins, losses)
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    q = c.execute('SELECT * FROM stats_redsdata')
    db = q.fetchone()
    w_db = db[1]
    l_db = db[2]

    # get record from reds for today
    URL = 'http://gd2.mlb.com/components/game/mlb/year_'+year+'/month_'+month+'/day_'+day+'/epg.xml'
    f = urllib2.urlopen(URL)
    xmld = minidom.parse(f).toxml()
    f.close()
    root = ET.fromstring(xmld)

    for game in root.findall('game'):
        if game.get('away_name_abbrev') == 'CIN':
            w_mlb = game.get('away_win')
            l_mlb = game.get('away_loss')
            break
        elif game.get('home_name_abbrev') == 'CIN':
            w_mlb = game.get('home_win')
            l_mlb = game.get('home_loss')
            break
        else:
            w_mlb = w_db
            l_mlb = l_db

    # if DB record <> MLB record
    if w_db != w_mlb and l_db != l_mlb:
        # delete DB record
        c.execute('DELETE from stats_redsdata')
        conn.commit()

        # add today's date, wins and loses
        c.execute('INSERT INTO stats_redsdata VALUES (?, ?, ?)', (today, w_mlb, l_mlb))
        conn.commit()

    # if DB record = MLB record then stop.
    c.close()

if __name__ == '__main__':
    main()
