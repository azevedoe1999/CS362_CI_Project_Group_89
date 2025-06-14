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

    lower_str = num_str.lower()

    # Check if it's a hexadecimal number
    if lower_str.startswith('0x') or lower_str.startswith('-0x'):
        return convert_hex(lower_str)
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
    hex_digits = hex_str[2:]

    # Check if there are any digits left after trimming
    if not hex_digits:
        return None

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
    # Special cases check
    if dec_str == '.' or dec_str == '-.':
        return None

    # Find if decimal number is negative
    is_negative = False
    if dec_str.startswith('-'):
        is_negative = True
        dec_str = dec_str[1:]  # Trim negative sign

    # Check for empty string after removing negative sign
    if not dec_str:
        return None

    # Normalize decimal point positions
    if dec_str.startswith('.'):
        dec_str = '0' + dec_str
    if dec_str.endswith('.'):
        dec_str = dec_str + '0'

    # Validate and process decimal string
    return process_decimal_string(dec_str, is_negative)


def process_decimal_string(dec_str, is_negative):
    """
    Helper function to process and validate decimal string.
    Args:
        dec_str (str): Decimal string to process
        is_negative (bool): Whether the number is negative
    Returns:
        int or float: The decimal value, or None if invalid format
    """
    is_float = False
    valid_dec = "0123456789"
    float_count = 0

    # Validate all characters
    for digit in dec_str:
        if digit not in valid_dec:
            if digit == '.' and float_count < 1:
                is_float = True
                float_count += 1
            else:
                return None

    # Convert to number
    if is_float:
        splits = dec_str.split('.')
        int_value = str_to_int(splits[0])
        frac_value = str_to_int(splits[1])

        # Normalize fractional part
        frac_value = frac_value / (10 ** len(splits[1]))
        result = int_value + frac_value
    else:
        result = str_to_int(dec_str)

    # Apply negative sign if needed
    if is_negative:
        result = -result

    return result


# function 2
def my_datetime(num_sec):
    """
    This function takes in an integer value that represents
    the number of seconds since the epoch: January 1st, 1970.
    The function takes num_sec and converts it to a date and
    returns it as a string with the following format: MM-DD-YYYY.
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
    This function must have the following header:
    def conv_endian(num, endian='big').
    This function takes in an integer value as num and
    converts it to a hexadecimal number.
    The endian type is determined by the flag endian.
    The function will return the converted number as a string.
    It has the following specifications:
        It may be assumed that num will always be an integer
        Must be able to handle negative values for num
        A value of big for endian will return a hexadecimal number
        that is big-endian
        A value of little for endian will return a hexadecimal number
        that is little-endian
        Any other values of endian will return None (n.b. this is not a string,
        but the actual None value)
        The returned string will have each byte separated by a space
        Each byte must be two characters in length
    """

    # set up variables
    HEX_DIGITS = "0123456789ABCDEF"  # hex digits table
    is_negative = False  # flag if nun is negative or not

    # if num is negative --> make num a postive so we can convert it
    # will add negative sign at end
    if num < 0:
        is_negative = True
        num = abs(num)

    # Dictionary for endian mapping
    endian_map = {"big": False, "little": True}
    if endian not in endian_map:
        return None

    hex_num = ""  # store hex number we get from num

    # if num is 0, return 0
    if num == 0:
        return "0"

    # convert num to hex and assign it to hex_num
    while num > 0:
        remainder = num % 16
        hex_num = HEX_DIGITS[remainder] + hex_num
        num //= 16

    # pad hex_num with leading 0 if uneven
    if len(hex_num) % 2 != 0:
        hex_num = "0" + hex_num

    # add spaces
    chunks = [hex_num[i: i + 2] for i in range(0, len(hex_num), 2)]
    hex_num = " ".join(chunks)

    # if endian flag is little --> reverse the byte order
    if endian_map[endian]:
        reverse = hex_num.split()
        hex_num = reverse[::-1]
        hex_num = " ".join(hex_num)

    # add back negative sign if num was negative
    return f"{'-' if is_negative else ''}{hex_num}"
