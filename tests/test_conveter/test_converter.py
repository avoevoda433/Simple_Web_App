import unittest
from converter.converter import c2f_convert, f2c_convert, check_value


class TestConverter(unittest.TestCase):

    def test_c2f_converter(self):
        self.assertEqual(c2f_convert(5.0), 41.0)
        self.assertEqual(c2f_convert(-17.78), 0.0)

    def test_f2c_converter(self):
        self.assertEqual(f2c_convert(41.0), 5.0)
        self.assertEqual(f2c_convert(0.0), -17.78)

    def test_check_value(self):
        self.assertEqual(check_value('5.0'), True)
        self.assertEqual(check_value('text'), False)
        self.assertEqual(check_value(['w', 5]), False)
        self.assertEqual(check_value({'f': 32}), False)


if __name__ == '__main__':
    unittest.main()
