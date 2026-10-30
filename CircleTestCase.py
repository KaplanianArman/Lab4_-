import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_negative_radius(self):
        r = -24
        with self.assertRaises(ValueError):
            area(r)
        with self.assertRaises(ValueError):
            perimeter(r)

    def test_negative_unit_radius(self):
        r = -1
        with self.assertRaises(ValueError):
            area(r)
        with self.assertRaises(ValueError):
            perimeter(r)

    def test_string_num(self):
        r = '24'
        with self.assertRaises(TypeError):
            area(r)
        with self.assertRaises(TypeError):
            perimeter(r)

    def test_string_word(self):
        r = 'abc'
        with self.assertRaises(TypeError):
            area(r)
        with self.assertRaises(TypeError):
            perimeter(r)

    def test_zero_radius(self):
        r = 0
        res_area = area(r)
        res_perimeter = perimeter(r)
        self.assertAlmostEqual(res_area, 0.0)
        self.assertAlmostEqual(res_perimeter, 0.0)

    def test_default(self):
        r = 24
        res_area = area(r)
        res_perimeter = perimeter(r)
        self.assertAlmostEqual(res_area, 1809.5573684677208)
        self.assertAlmostEqual(res_perimeter, 150.79644737231007)

    def test_big_num(self):
        r = 82398287238719
        res_area = area(r)
        res_perimeter = perimeter(r)
        self.assertAlmostEqual(res_area, 2.132977338930098e+28)
        self.assertAlmostEqual(res_perimeter, 517723707715082.44)

    def test_unit_radius(self):
        r = 1
        res_area = area(r)
        res_perimeter = perimeter(r)
        self.assertAlmostEqual(res_area, 3.141592653589793)
        self.assertAlmostEqual(res_perimeter, 6.283185307179586)