import datetime

#naive date time does not have enough information like timezones,daylight saving,etc.They are easier to work with
#aware date time they have enough information to determine timezone,daylight saving

#Naive Date Time

#Date- .date gives dates only we cannot get time with this
d=datetime.date(2002,7,14)                          #create a date year,month,date
tday=datetime.date.today()                          #get todays date
day=tday.weekday()                                  #get weekday  Monday-0  Sunday-6
day=tday.isoweekday()                               #get weekday  Monday-1  Sunday-7
year=tday.year                                      #get today's year
month=tday.month                                    #get today's month
day=tday.day                                        #get today's day

#time delta's is the difference between two dates and time
tdelta=datetime.timedelta(days=7)                   #days difference is mentioned
date=tday+tdelta                                    #gives date 7 days later
date=tday-tdelta                                    #gives date 7 days ago

#If we substract or add two dates we get time delta
bday=datetime.date(2023,7,14)
till_bday=bday-tday                                 #it gives us the day difference between two given dates
sec=till_bday.total_seconds()                       #gives total seconds between the two dates


#Time- .time time only we cannot get date
t=datetime.time(9,15,39,100)                        #creates time hour,minute,second,micro second.

#If we want to get both date and time simultaneously datetime.datetime is used 
t=datetime.datetime(2023,7,14,19,30,30,10000)       #we can access individual attributes too 
tdelta=datetime.timedelta(days=7,hours=3)
total=t+tdelta

dt_today=datetime.datetime.today()                  #gives current local date time with no timezone
dt_now=datetime.datetime.now()                      #gives current local date time with a timezone(by default no timezone is set)
dt_uctnow=datetime.datetime.utcnow()                #gives us current utc time


#Timezone aware date time uses utc
import pytz
dt=datetime.datetime(2023,7,14,19,30,30,10000,tzinfo=pytz.UTC)        #+00:00 that appears in output is utc offset

#create current utc time that is timezone aware
dt_now=datetime.datetime.now(tz=pytz.UTC)
dt_utcnow=datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
dt_here=dt_uctnow.astimezone(pytz.timezone('Asia/Kolkata'))           #change timezone

#print all timezones
# for tz in pytz.all_timezones:
#     print(tz)

#to apply naive date time timezone aware we need to run timezone localize function
dt_now=datetime.datetime.now()                                        #current naive date time
dt_east=dt_now.astimezone(pytz.timezone('US/Eastern'))
#print(dt_east)                                                       #it will give error as dt_now is naive date time and not timezone aware
tz_here=pytz.timezone('Asia/KOlkata')                                 #timezone
dt_now=tz_here.localize(dt_now)                                       #run the localize function and our dt_now is aware date time
dt_east=dt_now.astimezone(pytz.timezone('US/Eastern'))                #now dt_now is timezone aware thus can perform aware functionalities


#format to represent dates in various ways can be seen through documentation
date=dt_now.strftime('%B %d,%Y')                                      #B-month    d-date   Y-Year.It converts datetime to string

#to convert date time string into date time object
dt_str='July 08,2023'                                                 #date time as string thus date time operations cannot pe performed
date=datetime.datetime.strptime(dt_str,'%B %d,%Y')                    #parameters are date time string as well as format of the string