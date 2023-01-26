"""
sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(5,6)

        self.assertEqual(res,11)


def subtract(x,y):
    return y - x
    # def test_sub_numbers(self):
    #     """sub numbers"""
    #     res = calc.subtract(10,15)

    #     self.assertEqual(res, 5)