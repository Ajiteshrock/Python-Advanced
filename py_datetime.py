import datetime
d = datetime.date(2020,12,2)#YY-MM-DD
#for todays date

date_today = datetime.date.today()
print(date_today)
# now todays's day
# todays' weekday
# todays' is week day

print(date_today.day)#it will print 2 becuase monaday starts with 0
print(date_today.weekday())#it will print 2 becuase monaday starts with 0
print(date_today.isoweekday())#it will print 2 becuase monaday starts with 1 #remember all these carefully

#TIMEDELTA
tdelta = datetime.timedelta(days=7) #this 'tdelta' can reduce or increase a day +7 or -7
#for e.g

day = datetime.date.today()
print(day+tdelta) # will print 9th december because today is 2 december and after 7 days 
#it will be 9 december

print(day-tdelta) # will print the date 7 days before today


#now working with time

time = datetime.time(12,30,34,10000)
print(time)
print(time.hour)
print(time.minute)

#now working with datetime module
time_date = datetime.datetime.today()
time_date2 = datetime.datetime.now()
time_date3 = datetime.datetime.utcnow()

print(time_date) # without timezone
print(time_date2) # you can pass the timezone as well
print(time_date3)

import pytz #pytz stands for python timezone
#for tz in pytz.all_timezones:
    #rint(tz)

dt_india = time_date.astimezone(pytz.timezone('GMT'))
print(dt_india)

string = 'December 2 2020'
date = datetime.datetime.strptime(string,"%B %d %Y") #gazab
string_new = datetime.datetime.strftime(date,format="%B %d %Y")
print(date,string_new)