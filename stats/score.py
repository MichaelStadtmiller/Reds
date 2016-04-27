import time


def main():
    # create URL from mlb site
    # http://gd2.mlb.com/components/game/mlb/year_2016/month_06/day_30/epg.xml
    year = time.strftime("%Y")
    month = time.strftime("%m")
    day = time.strftime("%d")
    URL = 'http://gd2.mlb.com/components/game/mlb/year_'+year+'/month_'+month+'/day_'+day+'/epg.xml'

    # get redsdata from the database (date, wins, losses)

    # get record from reds for today

    # if DB record <> MLB record
        # delete DB record
        # add today's date, wins and loses
    # if DB record = MLB record then stop.


if __name__ == '__main__':
    main()
