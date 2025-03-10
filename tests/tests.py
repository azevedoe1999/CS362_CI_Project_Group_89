import unittest
import task

class TestCase(unittest.TestCase):
    # Black-box testing
    def test_integers(self):
        # Testing positive integers
        self.assertEqual(conv_num('0'), 0)
        self.assertEqual(conv_num('123'), 123)
        self.assertEqual(conv_num('9999'), 9999)
        
        # Testing negative integers
        self.assertEqual(conv_num('-1'), -1)
        self.assertEqual(conv_num('-456'), -456)
    
    def test_floating_point(self):
        # Testing standard format
        self.assertEqual(conv_num('123.45'), 123.45)
        self.assertEqual(conv_num('-123.45'), -123.45)
        
        # Testing leading decimal point
        self.assertEqual(conv_num('.45'), 0.45)
        self.assertEqual(conv_num('-.45'), -0.45)
        
        # Testing trailing decimal point
        self.assertEqual(conv_num('123.'), 123.0)
        self.assertEqual(conv_num('-123.'), -123.0)
        
        # Testing zero values
        self.assertEqual(conv_num('0.0'), 0.0)
        self.assertEqual(conv_num('-0.0'), -0.0)
    
    def test_hexadecimal(self):
        # Testing basic hex
        self.assertEqual(conv_num('0x0'), 0)
        self.assertEqual(conv_num('0x1'), 1)
        self.assertEqual(conv_num('0xA'), 10)
        self.assertEqual(conv_num('0xF'), 15)
        
        # Testing case-insensitivity
        self.assertEqual(conv_num('0xAD4'), 2772)
        self.assertEqual(conv_num('0Xad4'), 2772)
        self.assertEqual(conv_num('0xaD4'), 2772)
        
        # Testing negative hex
        self.assertEqual(conv_num('-0xAD4'), -2772)
        self.assertEqual(conv_num('-0xad4'), -2772)
        
        # Testing larger values
        self.assertEqual(conv_num('0xFFFF'), 65535)
    
    # White-box testing
    def test_return_type(self):
        # Ensure integers return as int type
        self.assertTrue(isinstance(conv_num('123'), int))
        self.assertTrue(isinstance(conv_num('-456'), int))
        self.assertTrue(isinstance(conv_num('0xAD4'), int))
        
        # Ensure floats return as float type
        self.assertTrue(isinstance(conv_num('123.45'), float))
        self.assertTrue(isinstance(conv_num('.45'), float))
        self.assertTrue(isinstance(conv_num('123.'), float))
    
    # Testing error cases
    def test_invalid_inputs(self):
        # Multiple decimal points
        self.assertIsNone(conv_num('12.3.45'))
        
        # Alpha in decimal
        self.assertIsNone(conv_num('12345A'))
        self.assertIsNone(conv_num('A12345'))
        
        # Invalid hex format
        self.assertIsNone(conv_num('0xAZ4'))
        self.assertIsNone(conv_num('AD4'))  # Missing 0x prefix
        
        # Empty or non-string inputs
        self.assertIsNone(conv_num(''))
        self.assertIsNone(conv_num(None))
        self.assertIsNone(conv_num(123))
    
    # Regression tests
    def test_regression_cases(self):
        # Edge cases from specifications
        self.assertEqual(conv_num('12345'), 12345)
        self.assertEqual(conv_num('-123.45'), -123.45)
        self.assertEqual(conv_num('.45'), 0.45)
        self.assertEqual(conv_num('123.'), 123.0)
        self.assertEqual(conv_num('0xAD4'), 2772)
        self.assertEqual(conv_num('0Xad4'), 2772)
        self.assertEqual(conv_num('-0xAD4'), -2772)
        
        # Additional edge cases
        self.assertEqual(conv_num('0'), 0)
        self.assertEqual(conv_num('-0'), 0)
        self.assertEqual(conv_num('0.0'), 0.0)

if __name__ == '__main__':
    unittest.main()
