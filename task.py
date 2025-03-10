# function 2
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
    YEAR = 1970
    MONTH = 1
    DAY = 1

    # set up variables for seconds in set amount duration
    SEC_IN_NON_LEAP_YEAR = 31536000
    SEC_IN_LEAP_YEAR = 31622400
    SEC_IN_DAY = 86400

    # set up array for days in each month
    MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # calculate how many years
    while num_sec >= SEC_IN_NON_LEAP_YEAR:
        if check_for_leap_year(YEAR):
            if num_sec >= SEC_IN_LEAP_YEAR:
                num_sec -= SEC_IN_LEAP_YEAR  # is leap year
            else:
                break
        else:
            num_sec -= SEC_IN_NON_LEAP_YEAR

        YEAR += 1

    # calculate how many months
    while num_sec >= SEC_IN_DAY:
        # gets current month
        if MONTH == 2:  # month of Feb
            if check_for_leap_year(YEAR):
                days = 29  # is leap year
            else:
                days = 28
        else:
            days = MONTHS[MONTH - 1]

        if num_sec >= days * SEC_IN_DAY:
            num_sec = num_sec - (days * SEC_IN_DAY)
            MONTH += 1
            if MONTH > 12:  # end of year --> add year & start at month 1 (Jan)
                MONTH = 1
                YEAR += 1
        else:
            break

    # calculate the day
    DAY = DAY + (num_sec // SEC_IN_DAY)

    # don't care about the remaining seconds

    # format the date
    return f"{MONTH:02d}-{DAY:02d}-{YEAR}"


# helper function for my_datetime (function 2)
def check_for_leap_year(year):
    """Check if given year is leap year"""
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True

    return False
