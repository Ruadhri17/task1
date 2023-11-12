from project.customers.models import Customer
import unittest

class TestCustomer(unittest.TestCase):
    def test_name_too_short_length(self):
        with self.assertRaises(ValueError):
            Customer('x', 'test', 18)
    def test_name_too_long_length(self):
        with self.assertRaises(ValueError):
            Customer('x'*65, 'test', 18)
    def test_name_proper_length(self):
        Customer('x'*30, 'test', 18)
    def test_name_allowed_characters(self):
        Customer('abc123:,-_', 'test', 18)
    def test_name_forbidden_characters(self):
        for c in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                '=', '+', '.', '/', '<', '>', '?', ';', '\'',
                '\\', '\"', '|', '[', ']', '{', '}', '`', '~']:
            with self.assertRaises(ValueError):
                Customer(c*4, 'test', 18)

    def test_city_too_short_length(self):
        with self.assertRaises(ValueError):
            Customer('test', 'x', 18)
    def test_city_too_long_length(self):
        with self.assertRaises(ValueError):
            Customer('test', 'x'*65, 18)
    def test_city_proper_length(self):
        Customer('test','x'*30, 18)
    def test_city_allowed_characters(self):
        Customer('test', 'abc123:,-_', 18)
    def test_city_forbidden_characters(self):
        for c in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                '=', '+', '.', '/', '<', '>', '?', ';', '\'',
                '\\', '\"', '|', '[', ']', '{', '}', '`', '~']:
            with self.assertRaises(ValueError):
                Customer('test', c*4, 18)

if __name__ == '__main__':
    unittest.main()