import unittest
import task


class TestCase(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
