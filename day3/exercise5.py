#Exercise 5 - Amount of time left until January 1st


import datetime

def time_until_new_year():
    now = datetime.datetime.now()

    next_year = now.year + 1
    new_year = datetime.datetime(next_year, 1, 1)

    difference = new_year - now

    print(difference)

time_until_new_year()