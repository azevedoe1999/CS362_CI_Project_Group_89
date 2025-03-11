# function 1
def conv_num(num_str):
    """
    This function converts a string to a base 10 number.
    Args:
        num_str (str): The string to convert
    Returns:
        int or float: The converted number, or None incase invalid format
    """
    # Check if input is valid
    if not isinstance(num_str, str) or num_str == '':
        return None

    # Check if it's a hexadecimal number
    if num_str.lower().startswith('0x') or num_str.lower().startswith('-0x'):
        return convert_hex(num_str)
    else:
        return convert_decimal(num_str)


def convert_hex(hex_str):
    """
    Converts a hexadecimal string to a decimal integer.
    Args:
        hex_str (str): The hexadecimal string to convert
    Returns:
        int: The decimal value, or None if invalid format
    """
    # Find if hex number is negative
    is_negative = False
    if hex_str.startswith('-'):
        is_negative = True
        hex_str = hex_str[1:]  # Trim negative sign

    # Trim 0x prefix
    hex_digits = hex_str[2:].lower()

    # Check if all characters are valid
    valid_hex = "0123456789abcdef"
    for digit in hex_digits:
        if digit not in valid_hex:
            return None

    # Conversion
    decimal_value = 0
    for digit in hex_digits:
        # Convert each hex digit to its decimal value
        if digit in "0123456789":
            digit_value = ord(digit) - ord('0')
        else:
            digit_value = ord(digit) - ord('a') + 10

        decimal_value = decimal_value * 16 + digit_value

    # Negate if needed
    if is_negative:
        decimal_value = -decimal_value

    return decimal_value


def str_to_int(digit_str):
    """
    Helper function to convert a string of digits to an integer.

    Args:
        digit_str (str): String containing only digits

    Returns:
        int: The integer value
    """
    int_value = 0
    for digit in digit_str:
        digit_value = ord(digit) - ord('0')
        int_value = int_value * 10 + digit_value
    return int_value


def convert_decimal(dec_str):
    """
    Converts a decimal string to a number.
    Args:
        dec_str (str): The decimal string to convert
    Returns:
        int or float: The decimal value, or None if invalid format
    """
    is_float = False  # Flag for float number

    # Find if decimal number is negative
    is_negative = False
    if dec_str.startswith('-'):
        is_negative = True
        dec_str = dec_str[1:]  # Trim negative sign

    # Normalize cases like .45
    if dec_str.startswith('.'):
        dec_str = '0' + dec_str

    # Normalize cases like 123.
    if dec_str.endswith('.'):
        dec_str = dec_str + '0'

    # Check if all characters are valid
    valid_dec = "0123456789"
    float_count = 0
    for digit in dec_str:
        if digit not in valid_dec:
            if digit == '.' and float_count < 1:
                is_float = True
                float_count = float_count + 1
            else:
                return None

    result = None
    if is_float:
        # Since it is float, split into two
        splits = dec_str.split('.')

        int_value = str_to_int(splits[0])

        frac_value = str_to_int(splits[1])

        # Normalize frac part
        frac_value = frac_value / (10 ** len(splits[1]))

        result = int_value + frac_value
        if is_negative:
            result = -result
    else:
        int_value = str_to_int(dec_str)

        if is_negative:
            result = -int_value

    return result


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
