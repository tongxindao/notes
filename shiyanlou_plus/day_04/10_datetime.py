from datetime import date, datetime, timedelta

print("today is: {0}".format(date.today()))
print("utc time is: {0}".format(datetime.utcnow()))

t = datetime.now()
print("today: {0}".format(t))
print("change format: {0}".format(datetime.strftime(t, "%Y-%m-%d %H:%M:%S")))
print(
    "change format1: {0}".format(
        datetime.strptime(
            "2017-11-18 22:57:01",
            "%Y-%m-%d %H:%M:%S")))
print(
    "datedelta time is: {0}".format(
        (t +
         timedelta(
             weeks=1,
             days=-
             3,
             hours=3,
             minutes=-
             10))))
print("the day is: {0}".format(t.day))
print("this year: {0}".format(t.year))
print("the minute is: {0}".format(t.minute))
