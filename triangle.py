import unittest

def area(a, h):
    '''
    Возвращает площадь треугольника

        Параметры:
            a (int) : целое положительное число (основание треугольника)
            h (int) : целое положительное число (высота треугольника)
        
        Возвращаемое значение:
            area (float) : вещественное положительное число (площадь треугольника)
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника

        Параметры:
            a (int) : целое положительное число (первая сторона треугольника)
            b (int) : целое положительное число (вторая сторона треугольника)
            c (int) : целое положительное число (третья сторона треугольника)
        
        Возвращаемое значение:
            perimeter (int) : целое положительное число (периметр треугольника)
    '''
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_zero_base(self):
        a, b, c, h = 0, 2, 3, 4
        res_area = area(a, h)
        res_perimetr = perimeter(a, b, c)
        self.assertEqual(res_area, 0.0)
        self.assertEqual(res_perimetr, 5)
        
    def test_zero_height(self):
        a, b, c, h = 1, 2, 3, 0
        res_area = area(a, h)
        res_perimetr = perimeter(a, b, c)
        self.assertEqual(res_area, 0.0)
        self.assertEqual(res_perimetr, 6)
       
    def test_default(self):
        a, b, c, h = 6, 4, 5, 2
        res_area = area(a, h)
        res_perimetr = perimeter(a, b, c)
        self.assertEqual(res_area, 6.0)
        self.assertEqual(res_perimetr, 15)

    def test_big_num(self):
        a, b, c, h = 19209102, 1098118, 19201920192, 290329092
        res_area = area(a, h)
        res_perimetr = perimeter(a, b, c)
        self.assertEqual(res_area, 2788480570897692.0)
        self.assertEqual(res_perimetr, 19222227412)

    def test_unit_base(self):
        a, b, c, h = 1, 3, 3, 6
        res_area = area(a, h)
        res_perimetr = perimeter(a, b, c)
        self.assertEqual(res_area, 3.0)
        self.assertEqual(res_perimetr, 7)

    def test_unit_height(self):
        a, b, c, h = 2, 4, 5, 1
        res_area = area(a, h)
        res_perimetr = perimeter(a, b, c)
        self.assertEqual(res_area, 1.0)
        self.assertEqual(res_perimetr, 11)