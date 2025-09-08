from datetime import datetime
from datetime import timedelta

# import datetime
# datetime.datetime

# now
# now.date
# now.time

# print(datetime.now())
# print(datetime.now().date())
# print(datetime.now().time())

# converting string to datetime
# date1 = datetime.date()
# print(date1)

# date1 = datetime(2025, 7, 10)
# date2 = datetime(2025, 8, 26)
# print(date2 - date1)

# date =  datetime.today().date()
# data = timedelta(300)

# print(date + data)


# Task:
#     * enter your dob in dd/mm/yyyy
#     * and find the age of the person in days

# dob = input("Enter dob in dd-mm-yyy: ")
# # "5-6-1999"
# day, month, year = dob.split("-")
# day = int(day)
# month = int(month)
# year = int(year)

# todaydate = datetime.now().date()
# dob_in_datetime = datetime(year, month, day).date()

# age_in_days = todaydate - dob_in_datetime

# print(age_in_days.days/365)

# given date
date_str = "3-10-2005"
date_obj = datetime.strptime(date_str, "%d-%m-%Y")

# get day name
day_name = date_obj.strftime("%A")

print(f"{date_str} was a {day_name}")

# Output: 3-10-1996 was a Thursday

