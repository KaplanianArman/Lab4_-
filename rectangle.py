import unittest

def area(a, b):
    '''
    Возвращает площадь прямоугольника

        Параметры:
            a (int) : целое положительное число (ширина прямоугольника)
            b (int) : целое положительное число (длина прямоугольника)
        
        Возвращаемое значение:
            area (int) : целое положительное число (площадь прямоугольника)
    '''
    return a * b


def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника

        Параметры:
            a (int) : целое положительное число (ширина прямоугольника)
            b (int) : целое положительное число (длина прямоугольника)
        
        Возвращаемое значение:
            perimeter (int) : целое положительное число (периметр прямоугольника)
    '''
    return (a + b) * 2

class RectangleTestCase(unittest.TestCase):
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