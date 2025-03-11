import unittest
import task


class TestCase(unittest.TestCase):
    """Test Cases for Function 2 (conv_num)"""

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


if __name__ == "__main__":
    unittest.main()
