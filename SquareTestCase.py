import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_negative_len(self):
        a = -5
        with self.assertRaises(ValueError):
            area(a)
        with self.assertRaises(ValueError):
            perimeter(a)

    def test_negative_big_num(self):
        a = -83219378127389173827198
        with self.assertRaises(ValueError):
            area(a)
        with self.assertRaises(ValueError):
            perimeter(a)

    def test_string_num(self):
        a = '12'
        with self.assertRaises(TypeError):
            area(a)
        with self.assertRaises(TypeError):
            perimeter(a)

    def test_string_word(self):
        a = 'abc'
        with self.assertRaises(TypeError):
            area(a)
        with self.assertRaises(TypeError):
            perimeter(a)

    def test_zero_len(self):
        a = 0
        res_area = area(a)
        res_perimeter = perimeter(a)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_default(self):
        a = 12
        res_area = area(a)
        res_perimeter = perimeter(a)
        self.assertEqual(res_area, 144)
        self.assertEqual(res_perimeter, 48)

    def test_big_num(self):
        a = 83219378127389173827198
        res_area = area(a)
        res_perimeter = perimeter(a)
        self.assertEqual(res_area, 6925464895909379635894595694064067938764531204)
        self.assertEqual(res_perimeter, 332877512509556695308792)

    def test_unit_len(self):
        a = 1
        res_area = area(a)
        res_perimeter = perimeter(a)
        self.assertEqual(res_area, 1)
        self.assertEqual(res_perimeter, 4)