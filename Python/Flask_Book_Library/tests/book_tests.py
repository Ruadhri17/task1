from project.books.models import Book
import unittest

class TestBook(unittest.TestCase):
    def test_name_too_short_length(self):
        with self.assertRaises(ValueError):
            Book('x', 'test', 2023, 'x', '2days')
    def test_name_too_long_length(self):
        with self.assertRaises(ValueError):
            Book('x'*65, 'test', 2023, 'x', '2days')
    def test_name_proper_length(self):
        Book('x'*30, 'test', 2023, 'x', '2days')
    def test_name_allowed_characters(self):
        Book('abc123:,-_', 'test', 2023, 'x', '2days')
    def test_name_forbidden_characters(self):
        for c in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                '=', '+', '.', '/', '<', '>', '?', ';', '\'',
                '\\', '\"', '|', '[', ']', '{', '}', '`', '~']:
            with self.assertRaises(ValueError):
                Book(c*4, 'test', 2023, 'x', '2days')

    def test_author_too_short_length(self):
        with self.assertRaises(ValueError):
            Book('test', 'x', 2023, 'x', '2days')
    def test_author_too_long_length(self):
        with self.assertRaises(ValueError):
            Book('test', 'x'*65, 2023, 'x', '2days')
    def test_author_proper_length(self):
        Book('test', 'x'*30, 2023, 'x', '2days')
    def test_author_allowed_characters(self):
        Book('test', 'abc123:,-_', 2023, 'x', '2days')
    def test_author_forbidden_characters(self):
        for c in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                '=', '+', '.', '/', '<', '>', '?', ';', '\'',
                '\\', '\"', '|', '[', ']', '{', '}', '`', '~']:
            with self.assertRaises(ValueError):
                Book('test', c*4, 2023, 'x', '2days')

if __name__ == '__main__':
    unittest.main()