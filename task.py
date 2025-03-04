"""
Reminders:
1. you are not permitted to use any Python built-in/library
2. you may write helper functions if you wish to assist with maintaining targeted code
"""


# Function 2
def my_datetime(num_sec):
    """
    This function takes in an integer value that represents the number of seconds since the epoch: January 1st, 1970.
    The function takes num_sec and converts it to a date and returns it as a string with the following format: MM-DD-YYYY.
    It has the following specifications:
        It may be assumed that num_sec will always be an int value
        It may be assumed that num_sec will always be a non-negative value
        Must be able to handle leap years
    """

    # set up variables to start of epoch
    year = 1970
    month = 1
    day = 1

    # set up array for days in each month
    days_in_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # calculate how many years
    while num_sec >= 31536000:  # seconds in a year
        # if particular year is a leap year
        if year % 4 == 0 and year % 100 != 0:
            # subtract seconds in a leap year from num_sec
            num_sec -= 31622400
        elif year % 400 == 0:
            num_sec -= 31622400
        else:
            # subtract seconds in a regular year from num_sec
            num_sec -= 31536000
        year += 1

    # calculate how many months
    while num_sec >= 86400:  # seconds in a day
        if month == 2:  # if month is Feburary
            # if particular year is a leap year
            if year % 4 == 0 and year % 100 != 0:
                days_in_month = 29
            elif year % 400 == 0:
                days_in_month = 29
            else:
                # not a leap year, so Feb has 28 days
                days_in_month = 28
        else:
            # for all the other months
            days_in_month = days_in_each_month[month - 1]

        if num_sec >= days_in_month * 86400:
            # subtract seconds in a given month from num_sec
            num_sec -= days_in_month * 86400
            month += 1
            # restart the month once it hit December (12) and add a year
            if month > 12:
                month = 1
                year += 1
        else:
            break

    # calculate the day
    day += num_sec // 86400
    num_sec %= 86400

    # formate the date
    return f"{month:02d}-{day:02d}-{year}"
