import unittest

def even_or_odd(num):
    return num%2==0




class test_odd_or_even(unittest.TestCase):
    def test_even(self):
        self.assertTrue(64%2==0)

    def test_odd(self):
        self.assertFalse(5%2!=0)
