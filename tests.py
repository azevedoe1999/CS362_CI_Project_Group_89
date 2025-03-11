import unittest
import task


class TestCaseFunction1(unittest.TestCase):
    """Test Cases for Function 1 (conv_num)"""

    # Black-box testing
    def test_function1_integers(self):
        # Testing positive integers
        self.assertEqual(task.conv_num('0'), 0)
        self.assertEqual(task.conv_num('123'), 123)
        self.assertEqual(task.conv_num('9999'), 9999)

        # Testing negative integers
        self.assertEqual(task.conv_num('-1'), -1)
        self.assertEqual(task.conv_num('-456'), -456)

    def test_function1_floating_point(self):
        # Testing standard format
        self.assertEqual(task.conv_num('123.45'), 123.45)
        self.assertEqual(task.conv_num('-123.45'), -123.45)

        # Testing leading decimal point
        self.assertEqual(task.conv_num('.45'), 0.45)
        self.assertEqual(task.conv_num('-.45'), -0.45)

        # Testing trailing decimal point
        self.assertEqual(task.conv_num('123.'), 123.0)
        self.assertEqual(task.conv_num('-123.'), -123.0)

        # Testing zero values
        self.assertEqual(task.conv_num('0.0'), 0.0)
        self.assertEqual(task.conv_num('-0.0'), -0.0)

    def test_function1_hexadecimal(self):
        # Testing basic hex
        self.assertEqual(task.conv_num('0x0'), 0)
        self.assertEqual(task.conv_num('0x1'), 1)
        self.assertEqual(task.conv_num('0xA'), 10)
        self.assertEqual(task.conv_num('0xF'), 15)

        # Testing case-insensitivity
        self.assertEqual(task.conv_num('0xAD4'), 2772)
        self.assertEqual(task.conv_num('0Xad4'), 2772)
        self.assertEqual(task.conv_num('0xaD4'), 2772)

        # Testing negative hex
        self.assertEqual(task.conv_num('-0xAD4'), -2772)
        self.assertEqual(task.conv_num('-0xad4'), -2772)

        # Testing larger values
        self.assertEqual(task.conv_num('0xFFFF'), 65535)

    # White-box testing
    def test_function1_return_type(self):
        # Ensure integers return as int type
        self.assertTrue(isinstance(task.conv_num('123'), int))
        self.assertTrue(isinstance(task.conv_num('-456'), int))
        self.assertTrue(isinstance(task.conv_num('0xAD4'), int))

        # Ensure floats return as float type
        self.assertTrue(isinstance(task.conv_num('123.45'), float))
        self.assertTrue(isinstance(task.conv_num('.45'), float))
        self.assertTrue(isinstance(task.conv_num('123.'), float))

    # Testing error cases
    def test_function1_invalid_inputs(self):
        # Multiple decimal points
        self.assertIsNone(task.conv_num('12.3.45'))

        # Alpha in decimal
        self.assertIsNone(task.conv_num('12345A'))
        self.assertIsNone(task.conv_num('A12345'))

        # Invalid hex format
        self.assertIsNone(task.conv_num('0xAZ4'))
        self.assertIsNone(task.conv_num('AD4'))  # Missing 0x prefix

        # Empty or non-string inputs
        self.assertIsNone(task.conv_num(''))
        self.assertIsNone(task.conv_num(None))
        self.assertIsNone(task.conv_num(123))

        # Attempting to parse a hex number with a decimal part
        self.assertIsNone(task.conv_num('0xFF.02'))
        self.assertIsNone(task.conv_num('-0x1F.4'))
        self.assertIsNone(task.conv_num('-0xFF.02'))
        self.assertIsNone(task.conv_num('0x.FF'))

        # Just "0x" with no digits
        self.assertIsNone(task.conv_num('0x'))
        self.assertIsNone(task.conv_num('-0x'))

        self.assertIsNone(task.conv_num(" 123"))
        self.assertIsNone(task.conv_num("123 "))

    def test_function1_large_numbers(self):
        """Test conversion of very large numbers to ensure correct handling of edge cases near integer limits."""
        # Very large numbers
        self.assertEqual(task.conv_num('9223372036854775807'),
                         9223372036854775807)  # Max 64-bit signed int
        self.assertEqual(task.conv_num('0xFFFFFFFFFFFFFFFF'),
                         18446744073709551615)  # Max 64-bit unsigned int

    def test_function1_edge_hex_cases(self):
        """Test edge cases for hexadecimal conversion including zero, negative zero, and padded numbers."""
        # Edge cases for hexadecimal
        self.assertEqual(task.conv_num('0x0'), 0)
        self.assertEqual(task.conv_num('-0x0'), 0)
        self.assertEqual(task.conv_num('0x000001'), 1)

    def test_function1_leading_zeros(self):
        """Test that numbers with leading zeros are correctly converted to their proper value."""
        # Numbers with leading zeros
        self.assertEqual(task.conv_num('00123'), 123)
        self.assertEqual(task.conv_num('000.123'), 0.123)
        self.assertEqual(task.conv_num('-00123'), -123)

    def test_function1_mixed_format_validation(self):
        """Test that invalid mixed formats are properly rejected and return None."""
        self.assertIsNone(task.conv_num('123-456')
                          )  # Invalid: digits with embedded dash
        # Invalid: digits with embedded plus
        self.assertIsNone(task.conv_num('123+456'))
        # Invalid: dash after prefix
        self.assertIsNone(task.conv_num('0x-123'))
        self.assertIsNone(task.conv_num('0x123-'))   # Invalid: trailing dash

    def test_function1_incomplete_hex_prefix(self):
        """Test incomplete hexadecimal prefixes"""
        self.assertIsNone(task.conv_num('0x'))     # Only prefix, no hex digits
        # Negative sign with only prefix
        self.assertIsNone(task.conv_num('-0x'))
        # Just zero (valid decimal, not hex)
        self.assertIsNone(task.conv_num('0'))
        self.assertIsNone(task.conv_num('x123'))   # Missing '0' in prefix
        self.assertIsNone(task.conv_num('0X'))     # Only prefix with capital X

    def test_function1_whitespace_handling(self):
        """Test strings with whitespace"""
        # Leading whitespace
        self.assertIsNone(task.conv_num(' 123'))    # Leading space
        self.assertIsNone(task.conv_num('\t123'))   # Leading tab
        self.assertIsNone(task.conv_num('\n123'))   # Leading newline

        # Trailing whitespace
        self.assertIsNone(task.conv_num('123 '))    # Trailing space
        self.assertIsNone(task.conv_num('123\t'))   # Trailing tab
        self.assertIsNone(task.conv_num('123\n'))   # Trailing newline

        # Whitespace around hex prefixes
        self.assertIsNone(task.conv_num(' 0x123'))  # Space before hex
        self.assertIsNone(task.conv_num('0x123 '))  # Space after hex

        # Whitespace in the middle
        # Space in the middle of decimal
        self.assertIsNone(task.conv_num('12 34'))
        # Space in the middle of hex
        self.assertIsNone(task.conv_num('0x12 34'))
        self.assertIsNone(task.conv_num('12.3 4'))  # Space after decimal point

    def test_function1_mixed_whitespace_and_prefix(self):
        """Test combinations of whitespace and prefix issues"""
        self.assertIsNone(task.conv_num('0 x123'))  # Space between '0' and 'x'
        # Space between '-0' and 'x'
        self.assertIsNone(task.conv_num('-0 x123'))
        # Space between '-' and '0x'
        self.assertIsNone(task.conv_num('- 0x123'))
        self.assertIsNone(task.conv_num('0x 123'))  # Space after prefix

    # Regression tests
    def test_function1_regression_cases(self):
        # Edge cases from specifications
        self.assertEqual(task.conv_num('12345'), 12345)
        self.assertEqual(task.conv_num('-123.45'), -123.45)
        self.assertEqual(task.conv_num('.45'), 0.45)
        self.assertEqual(task.conv_num('123.'), 123.0)
        self.assertEqual(task.conv_num('0xAD4'), 2772)
        self.assertEqual(task.conv_num('0Xad4'), 2772)
        self.assertEqual(task.conv_num('-0xAD4'), -2772)

        # Additional edge cases
        self.assertEqual(task.conv_num('0'), 0)
        self.assertEqual(task.conv_num('-0'), 0)
        self.assertEqual(task.conv_num('0.0'), 0.0)
        self.assertEqual(task.conv_num('00123'), 123)


class TestCaseFunction2(unittest.TestCase):
    """Test Cases for Function 2 (my_datetime)"""

    def test_1_function_2(self):
        """From examples"""
        s = 0  # input
        expected = "01-01-1970"
        self.assertEqual(task.my_datetime(s), expected)

    def test_2_function_2(self):
        """From examples"""
        s = 123456789  # input
        expected = "11-29-1973"
        self.assertEqual(task.my_datetime(s), expected)

    def test_3_function_2(self):
        """From examples"""
        s = 9876543210  # input
        expected = "12-22-2282"
        self.assertEqual(task.my_datetime(s), expected)

    def test_4_function_2(self):
        """From examples"""
        s = 201653971200  # input
        expected = "02-29-8360"
        self.assertEqual(task.my_datetime(s), expected)

    def test_5_function_2(self):
        """One day later"""
        s = 86400  # input
        expected = "01-02-1970"
        self.assertEqual(task.my_datetime(s), expected)

    def test_6_function_2(self):
        """One year later"""
        s = 31654800  # input
        expected = "01-02-1971"
        self.assertEqual(task.my_datetime(s), expected)

    def test_7_function_2(self):
        """End of leap year"""
        s = 94640400  # input
        expected = "12-31-1972"
        self.assertEqual(task.my_datetime(s), expected)

    def test_8_function_2(self):
        """Checks 02-29-1972, since 1972 is a leap year"""
        s = 68169600  # input
        expected = "02-29-1972"
        self.assertEqual(task.my_datetime(s), expected)

    def test_9_function_2(self):
        """Checks 02-28-1971, since 1971 is not a leap year"""
        s = 36579600  # input
        expected = "02-28-1971"
        self.assertEqual(task.my_datetime(s), expected)

    def test_10_function_2(self):
        """Checks 02-28-2100, since 2100 is not a leap year (not divisible by 400)"""
        s = 4107488400  # input
        expected = "02-28-2100"
        self.assertEqual(task.my_datetime(s), expected)

    def test_11_function_2(self):
        """Test year 2000 leap year"""
        s = 951782400  # 2000-02-29
        expected = "02-29-2000"
        self.assertEqual(task.my_datetime(s), expected)

    def test_12_function_2(self):
        """Test transition between months with different lengths"""
        # January 31 to February 1, 1970
        s_jan31 = 2678399  # 1970-01-31 23:59:59
        self.assertEqual(task.my_datetime(s_jan31), "01-31-1970")

        s_feb1 = 2678400  # 1970-02-01 00:00:00
        self.assertEqual(task.my_datetime(s_feb1), "02-01-1970")

    def test_13_function_2(self):
        """Test transition from December 31 to January 1"""
        # December 31, 1970 to January 1, 1971
        s_dec31 = 31535999  # 1970-12-31 23:59:59
        self.assertEqual(task.my_datetime(s_dec31), "12-31-1970")

        s_jan1 = 31536000  # 1971-01-01 00:00:00
        self.assertEqual(task.my_datetime(s_jan1), "01-01-1971")

    def test_14_function_2_day_boundary(self):
        """
        Tests that 23:59:59 on Jan 1, 1970 still returns 01-01-1970
        and doesn't roll over to 01-02-1970 by mistake.
        """
        s = 86399  # 23:59:59 on 1970-01-01
        expected = "01-01-1970"
        self.assertEqual(task.my_datetime(s), expected)

    def test_15_function_2(self):
        """Test with very large number of seconds (far future)"""
        s = 9999999999999  # Over 300 million years from epoch
        expected = "11-16-316887308"
        self.assertEqual(task.my_datetime(s), expected)

    def test_16_function_2(self):
        """Test with seconds that are exactly at month boundaries"""
        # Test exactly at March 1st in non-leap year
        s = 36720000  # 1971-03-01 00:00:00
        self.assertEqual(task.my_datetime(s), "03-01-1971")

        # Test exactly at March 1st in leap year
        s = 68256000  # 1972-03-01 00:00:00
        self.assertEqual(task.my_datetime(s), "03-01-1972")


class TestCaseFunction3(unittest.TestCase):
    """Test Cases for Function 3 (conv_endian)"""

    def test_1_function_3(self):
        """From example"""
        num = 954786
        endian = "big"
        expected = "0E 91 A2"
        self.assertEqual(task.conv_endian(num, endian), expected)

    def test_2_function_3(self):
        """From example"""
        num = 954786
        expected = "0E 91 A2"
        self.assertEqual(task.conv_endian(num), expected)

    def test_3_function_3(self):
        """From example"""
        num = -954786
        expected = "-0E 91 A2"
        self.assertEqual(task.conv_endian(num), expected)

    def test_4_function_3(self):
        """From example"""
        num = 954786
        endian = "little"
        expected = "A2 91 0E"
        self.assertEqual(task.conv_endian(num, endian), expected)

    def test_5_function_3(self):
        """From example"""
        num = -954786
        endian = "little"
        expected = "-A2 91 0E"
        self.assertEqual(task.conv_endian(num, endian), expected)

    def test_6_function_3(self):
        """From example"""
        num = -954786
        endian = "small"
        expected = None
        self.assertEqual(task.conv_endian(num, endian), expected)

    def test_7_function_3(self):
        """If num is 0"""
        num = 0
        expected = "0"
        self.assertEqual(task.conv_endian(num), expected)

    def test_8_function_3(self):
        """Checks smallest 1-byte"""
        self.assertEqual(task.conv_endian(15), "0F")
        self.assertEqual(task.conv_endian(15, "little"), "0F")

    def test_9_function_3(self):
        """Checks smallest 2-byte"""
        self.assertEqual(task.conv_endian(255), "FF")
        self.assertEqual(task.conv_endian(255, "little"), "FF")

    def test_10_function_3(self):
        """Checks largest 2-byte number"""
        self.assertEqual(task.conv_endian(65535), "FF FF")
        self.assertEqual(task.conv_endian(65535, "little"), "FF FF")

    def test_11_function_3(self):
        """Checks negative single-byte"""
        self.assertEqual(task.conv_endian(-255), "-FF")
        self.assertEqual(task.conv_endian(-255, "little"), "-FF")

    def test_12_function_3(self):
        """Checks for invalid endian"""
        self.assertEqual(task.conv_endian(100, ""), None)
        self.assertEqual(task.conv_endian(100, None), None)

    def test_13_function_3(self):
        """Checks values that would produce odd hex digit counts"""
        # 10A - needs padding and spacing
        self.assertEqual(task.conv_endian(266), "01 0A")
        # 100F - tests spacing mid-number
        self.assertEqual(task.conv_endian(4111), "10 0F")

    def test_14_function_3(self):
        """Tests 3-byte values with specific spacing requirements"""
        self.assertEqual(task.conv_endian(1118481), "11 11 11")
        self.assertEqual(task.conv_endian(1118481, "little"), "11 11 11")

    def test_15_function_3(self):
        """Tests with larger numbers to verify byte splitting"""
        # A 4-byte integer
        self.assertEqual(task.conv_endian(16777216), "01 00 00 00")
        self.assertEqual(task.conv_endian(16777216, "little"), "00 00 00 01")

        # A 5-byte integer
        self.assertEqual(task.conv_endian(4294967296), "01 00 00 00 00")
        self.assertEqual(task.conv_endian(
            4294967296, "little"), "00 00 00 00 01")

    def test_16_function_3(self):
        """Tests with non-standard sizes that could expose padding issues"""
        # This tests correct handling of a number that would produce '0A 0B 0C'
        self.assertEqual(task.conv_endian(658188), "0A 0B 0C")
        self.assertEqual(task.conv_endian(658188, "little"), "0C 0B 0A")

        # Test with a value that's on the boundary between byte sizes
        self.assertEqual(task.conv_endian(256), "01 00")
        self.assertEqual(task.conv_endian(256, "little"), "00 01")

    def test_17_function_3(self):
        """Test with negative zero-edge case"""
        self.assertEqual(task.conv_endian(-0),
                         "0")  # Should be treated as positive zero


if __name__ == "__main__":
    unittest.main()
