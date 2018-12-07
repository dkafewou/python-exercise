import unittest
from src.three_five import three_five


class TestThreeFiveFunction(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(three_five(1), '1')
        self.assertEqual(three_five(3), 'Three')
        self.assertEqual(three_five(5), 'Five')
        self.assertEqual(three_five(15), 'ThreeFive')


if __name__ == '__main__':
    unittest.main()
