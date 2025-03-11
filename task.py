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


# function 3
def conv_endian(num, endian="big"):
    """
    This function must have the following header: def conv_endian(num, endian='big').
    This function takes in an integer value as num and converts it to a hexadecimal number.
    The endian type is determined by the flag endian.
    The function will return the converted number as a string.
    It has the following specifications:
        It may be assumed that num will always be an integer
        Must be able to handle negative values for num
        A value of big for endian will return a hexadecimal number that is big-endian
        A value of little for endian will return a hexadecimal number that is little-endian
        Any other values of endian will return None (n.b. this is not a string, but the actual None value)
        The returned string will have each byte separated by a space
        Each byte must be two characters in length
    """

    # set up variables
    HEX_DIGITS = "0123456789ABCDEF"  # hex digits table
    NEGATIVE = False  # flag if nun is negative or not

    # if num is negative --> make num a postive so we can convert it
    # will add negative sign at end
    if num < 0:
        NEGATIVE = True
        num = abs(num)

    # check if endian is vaild --> if not, return None
    if endian != "big" and endian != "little":
        return None

    hex_num = ""  # store hex number we get from num

    # if num is 0, return 0
    if num == 0:
        hex_num = "0"
        return hex_num

    # convert num to hex and assign it to hex_num
    while num > 0:
        r = num % 16
        hex_num = HEX_DIGITS[r] + hex_num
        num //= 16

    # pad hex_num with leading 0 if uneven
    if len(hex_num) % 2 != 0:
        hex_num = "0" + hex_num

    # add spaces
    add_spaces = ""
    for i in range(len(hex_num)):
        if i > 0 and i % 2 == 0:
            add_spaces += " "
            add_spaces += hex_num[i]
        else:
            add_spaces += hex_num[i]

    hex_num = add_spaces

    # if endian flag is little --> reverse the byte order
    if endian == "little":
        reverse = hex_num.split()
        hex_num = reverse[::-1]
        hex_num = " ".join(hex_num)

    # add back negative sign if num was negative
    if NEGATIVE:
        hex_num = "-" + hex_num

    return hex_num
