########################################### Calendar Module ################################################
"""
You are given a date. Your task is to find what the day is on that date.
input:
08 05 2015
output:
WEDNESDAY
"""
import calendar
days = ['MONDAY', 'THUESDAY', 'WEDNESDAY', 'THURSDAY','FRIDAY','SATURDAY', 'SUNDAY']
month, day, year = input().split()
index_day = calendar.weekday(int(year), int(month), int(day))
print(days[index_day])
################# Second solution ########################
month, day, year = map(int, input().split())
print(calendar.day_name[calendar.weekday(year, month, day)].upper())