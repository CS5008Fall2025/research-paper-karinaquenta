"""
This test file contains unit testing for the Rabin-Karp string search algorithm.
The tests verify that the algorithm finds patterns in a variety
of cases: multiple matches, overlapping matches, no matches,
and edge cases (like empty patterns and patterns longer than the text).

To run the tests, use the following in your terminal: python3 rabin_karp_test.py or python3 -m unittest rabin_karp_test.py 
"""
import unittest
from rabin_karp import rabin_karp


class TestRabinKarp(unittest.TestCase):

    def test_multiple_matches(self):
        self.assertEqual(rabin_karp("abracadabra", "abra"), [0, 7])

    def test_overlapping_matches(self):
        self.assertEqual(rabin_karp("aaaaa", "aa"), [0, 1, 2, 3])

    def test_single_match(self):
        self.assertEqual(rabin_karp("hello world", "world"), [6])

    def test_no_match(self):
        self.assertEqual(rabin_karp("abcdef", "xyz"), [])

    def test_pattern_longer_than_text(self):
        self.assertEqual(rabin_karp("short", "muchlonger"), [])

    def test_empty_pattern(self):
        self.assertEqual(rabin_karp("anything", ""), [])


if __name__ == "__main__":
    unittest.main()
