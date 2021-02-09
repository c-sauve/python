#!/usr/bin/python3

'''
Problem 19

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''


# I'm sure python has some type of library to calculate the date but i'd like to code up my own solution first.

months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

century = 100
start_date = 1
start_month = "January"
year = 1901
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
occurrence = 0
end_year = 2000
month = 0
#Tuesday was the weekday for January 1 1991
day = 2



#if day > 7:
#    day = 0
#
#if (year >= 2000) and (year < 1900):
#    pass




def is_leap_year(var_year):
    leap_year = False
    if year % 4 == 0:
        leap_year = True
    if year % century == 0:
        if year % 400 == 0:
            leap_year = True
    return leap_year


def occurrence_in_month(var_month, var_day_name, var_year, var_day, var_day_of_occurence):
    occurrence = 0
    check_day = var_day
    add_day = 0
    if is_leap_year(var_year):
        if months[var_month] == 'Febuary':
            add_day = 1
    for i in range(1, months[var_month] + add_day):
        if check_day > 6:
            check_day = 0
        if days[check_day] == var_day_name:
            if i == var_day_of_occurence:
                occurrence += 1
        check_day += 1
    return occurrence


while year < end_year + 1:
    #print(year)
    check_day = day
    add_day = 0
    current_month = list(months.keys())[month]
    if is_leap_year(year):
        if current_month == 'Febuary':
            add_day = 1
    for i in range(1, months[current_month] + add_day + 1):
        if check_day > 6:
            check_day = 0
        if days[check_day] == 'Sunday':
            if i == 1:
                occurrence += 1
        #print(current_month, days[check_day], i, year)
        check_day += 1
    month += 1
    if month > 11:
        month = 0
        year += 1
    day = check_day

print(occurrence)


# Maybe we should create a dictionary for every year and the day / months/ weekday within that dictionary...?