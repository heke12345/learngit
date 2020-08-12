import datetime as dt
import time as tm
print(tm.time())
print([1, 3]+[3, 7])
print("hh"+str(2))
dtnow = dt.datetime.fromtimestamp(tm.time())
# get year, month, day, etc.from a datetime
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second
delta = dt.timedelta(days=-100, hours=2)  # create a timedelta of 100 days
print(delta)
today = dt.date.today()  # 现在的本地时间
print(today)
n = today+delta  # the date 100 days ago
print(n)
print(today > n)  # compare dates
