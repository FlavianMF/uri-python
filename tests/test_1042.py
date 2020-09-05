import unittest


def simpleSort(array):

    return 1


class Test_SimpleSort(unittest.TestCase):
    def test_1(self):
        self.assertEqual(simpleSort([7, 21, -14]), [-14, 7, 21])
