import unittest   # The test framework


def CalculateCircleArea(radius):
    a = 3.14159 * (float(radius) * float(radius))

    return round(a, 4)


class Test_CalculateCircleArea(unittest.TestCase):
    def test_1(self):
        self.assertEqual(CalculateCircleArea(2), 12.5664)

    def test_2(self):
        self.assertEqual(CalculateCircleArea(100.64), 31819.3103)


if __name__ == '__main__':
    unittest.main()
