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

    1 year(nonleap) = 31,536,000s
    1 year(leap) = 31,622,400s
    1 day = 86,400s
    1 month = days_in_month * 86,400s
    """

    # set up variables to start of epoch
    year = 1970
    month = 1
    day = 1

    # set up array for days in each month
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # calculate how many years
    while num_sec >= 31536000:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if num_sec >= 31622400:
                num_sec -= 31622400  # is leap year
            else:
                break
        else:
            num_sec -= 31536000
            
        year += 1

    # calculate how many months
    while num_sec >= 86400:
        # gets current month
        if month == 2:  # month of Feb
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                days = 29  # is leap year
            else:
                days = 28
        else:
            days = months[month - 1]

        if num_sec >= days * 86400:
            num_sec = num_sec - (days * 86400)
            month += 1
            if month > 12:  # end of year --> add year & start at month 1 (Jan)
                month = 1
                year += 1
        else:
            break

    # calculate the day
    day = day + (num_sec // 86400)

    # don't care about the remaining seconds

    # formate the date
    return f"{month:02d}-{day:02d}-{year}"
