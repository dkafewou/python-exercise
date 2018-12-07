import unittest
from three_five import three_five
from postcode import Postcode, ValidationError


class TestThreeFiveFunction(unittest.TestCase):

    def test_three_five(self):
        self.assertEqual(three_five(1), '1')
        self.assertEqual(three_five(3), 'Three')
        self.assertEqual(three_five(5), 'Five')
        self.assertEqual(three_five(15), 'ThreeFive')


class TestPostcode(unittest.TestCase):
    def setUp(self):
        self.postcode = Postcode('SW1W 0NY')

    def test_get_outward_code(self):
        self.assertEqual(self.postcode.get_outward_code(), 'SW1W')

    def test_get_inward_code(self):
        self.assertEqual(self.postcode.get_inward_code(), '0NY')

    def test_is_valid(self):
        self.assertEqual(Postcode.is_valid('SW1W 0NY'), True)
        self.assertEqual(Postcode.is_valid('L1 8JQ'), True)
        self.assertEqual(Postcode.is_valid('1 8JQ'), False)
        self.assertEqual(Postcode.is_valid('1W1W 0NY'), False)

    def test_format(self):
        self.assertEqual(Postcode.format('1W1W0NY'), '1W1W 0NY')
        self.assertIs(type(Postcode.format('1W1W0NY')), str)

    def test_format_error(self):
        with self.assertRaises(ValidationError):
            Postcode.format('1W1W')


if __name__ == '__main__':
    unittest.main()
