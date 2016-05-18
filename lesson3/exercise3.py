# Level 1
# third exercise

from datetime import datetime

formats = ('%d %b %Y', '%d %B %Y', '%d.%m.%Y', '%m/%d/%y')


def date_conversion(date):
    for f in formats:
        try:
            dt = datetime.strptime(date, f).date()
            print(dt)
        except ValueError:
            pass

dates = ('11 Jan 2016', '4 April 2011', '11.03.2014', '03/24/91')

for d in dates:
    date_conversion(d)
