import unittest

from book import Book


class TestBook(unittest.TestCase):
    def setUp(self) -> None:
        self.book_1 = Book('Raven', 'Edgar Allan Poe', '01 Jan 1888')
        self.book_2 = Book('Raven2', 'Edgar Allan Poe2', '01 Jan 1888')

    def test_to_string(self):

        self.assertEqual(self.book_1.to_string(), 'Raven - Edgar Allan Poe', 'wrong formatting')
        self.assertEqual(self.book_2.to_string(), 'Raven2 - Edgar Allan Poe2', 'wrong formatting')

    def tearDown(self) -> None:
        del self.book_1
        del self.book_2
