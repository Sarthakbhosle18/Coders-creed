import datetime
import time

d1 = datetime.datetime.now()
d2 = datetime.datetime(year=2005, month=12, day=10, hour=0, minute=0, second=0)
print(d1)

print("minus date and time: ", d1-d2)

d3 = d1.strftime("%a %d-%b-%Y %I:%M %p")
print(d3)

while True:
    d4 = datetime.datetime.now()
    print(d4.strftime("%I:%M:%S %p %a"))
    time.sleep(1)