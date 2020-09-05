import unittest


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


class Test_Sample(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fibonacci(3), 2)

    def test_2(self):
        self.assertEqual(fibonacci(4), 3)
