import unittest


def fatorial(n):
    a = 1
    for i in range(1, n+1, 1):
        a *= i
    return a


class Test_Factorial(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fatorial(5), 120)
