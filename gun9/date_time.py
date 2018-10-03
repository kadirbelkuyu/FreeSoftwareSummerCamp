import datetime
from datetime import timedelta

date = datetime.datetime

print(date.today().month)
print(date.today().year)
print(date.today().microsecond)
print(date.today().second)
print(date.today() + datetime.timedelta(days=7, minutes=30))