import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_negative_width(self):
        w, h = -10, 20
        with self.assertRaises(ValueError):
            area(w, h)
        with self.assertRaises(ValueError):
            perimeter(w, h)

    def test_negative_both(self):
        w, h = -10, -20
        with self.assertRaises(ValueError):
            area(w, h)
        with self.assertRaises(ValueError):
            perimeter(w, h)

    def test_string_width(self):
        w, h = '10', 20
        with self.assertRaises(TypeError):
            area(w, h)
        with self.assertRaises(TypeError):
            perimeter(w, h)

    def test_string_both(self):
        w, h = 'abc', 'def'
        with self.assertRaises(TypeError):
            area(w, h)
        with self.assertRaises(TypeError):
            perimeter(w, h)

    def test_zero_width(self):
        w, h = 0, 10
        res_area = area(w, h)
        res_perimeter = perimeter(w, h)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 20)

    def test_zero_height(self):
        w, h = 20, 0
        res_area = area(w, h)
        res_perimeter = perimeter(w, h)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 40)

    def test_square(self):
        w, h = 10, 10
        res_area = area(w, h)
        res_perimeter = perimeter(w, h)
        self.assertEqual(res_area, 100)
        self.assertEqual(res_perimeter, 40)

    def test_big_num(self):
        w, h = 1190299, 19029109
        res_area = area(w, h)
        res_perimeter = perimeter(w, h)
        self.assertEqual(res_area, 22650329413591)
        self.assertEqual(res_perimeter, 40438816)

    def test_unit_width(self):
        w, h = 1, 902181
        res_area = area(w, h)
        res_perimeter = perimeter(w, h)
        self.assertEqual(res_area, 902181)
        self.assertEqual(res_perimeter, 1804364)

    def test_unit_height(self):
        w, h = 9219289832, 1
        res_area = area(w, h)
        res_perimeter = perimeter(w, h)
        self.assertEqual(res_area, 9219289832)
        self.assertEqual(res_perimeter, 18438579666)