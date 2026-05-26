#Exercise 6 - Birthday and minutes

import datetime

def minutes_lived(birthdate_str):
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
    now = datetime.datetime.now()

    difference = now - birthdate
    minutes = difference.total_seconds() / 60

    print(int(minutes))

# example usage
minutes_lived("2000-01-01")