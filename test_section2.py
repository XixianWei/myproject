# 2.2 Make a new test file and write comprehensive unit tests for the function you wrote in 2.1
# For each test case add a comment stating why you chose that case.

import unittest
from section2 import is_isogram

class TestMain(unittest.TestCase):

    def test_isogram(self):
        # To test a basic isogram.
        self.assertTrue(is_isogram("isogram"))

        # To test a longer isogram, chosen to verify function handles longer strings.
        self.assertTrue(is_isogram("uncopyrightable"))

        # To test a non-isogram word.
        self.assertFalse(is_isogram("aabbcc"))

        # To test an empty string, which is technically an isogram.
        self.assertTrue(is_isogram(""))

        # To test case sensitivity
        self.assertTrue(is_isogram("AmbideXtrouSly"))

        # To test word with non-letter characters, where these should be considered in the isogram check.
        self.assertFalse(is_isogram("hello-world"))

        # To test an integer input, chosen to verify function raises exception for non-string inputs.
        with self.assertRaises(ValueError):
            is_isogram(12345)
        
        # To test a list input.
        with self.assertRaises(ValueError):
            is_isogram(['isogram'])


if __name__ == '__main__':
    unittest.main()
