import datetime
d=datetime.date(2016,12,31)

print(d.weekday())

print(d.isoweekday())

delta=datetime.timedelta(days=7)

today=datetime.date.today()

print(today-d) # print the difference of the days between
print(d)


t=datetime.time(9,30,20,1000)

print(t)


d1=datetime.datetime.now() #allows to pass the timezone
utc_now = datetime.datetime.now(datetime.timezone.utc)

d3=datetime.datetime.today() # prints the current time with the current time zone


print(d1) #
print(utc_now) #
print(d3) #

