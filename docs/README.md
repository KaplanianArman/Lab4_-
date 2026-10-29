# *MATH FORMULAS*

## *SQUARE*
### *AREA*
$S = a^2$

```python
def area(a):
    return a * a
```

#### *Параметры:*
a (int) : целое положительное число (сторона квадрата)

#### *Возвращаемое значение:*
area (int) : целое положительное число (площадь квадрата)


#### *Примеры вызова функции:*
area(3) = 3 * 3 = 9\
area(5) = 5 * 5 = 25

### *PERIMETER*
$P = 4 \cdot a$

```python
def perimeter(a):
    return 4 * a
```

#### *Параметры:*
a (int) : целое положительное число (сторона квадрата)

#### *Возвращаемое значение:*
perimeter (int) : целое положительное число (периметр квадрата)

#### *Примеры вызова функции:*
perimeter(3) = 4 * 3 = 12\
perimeter(5) = 4 * 5 = 20


## *RECTANGLE*
### *AREA*
$S = a \cdot b$

```python
def area(a, b):
    return a * b
```

#### *Параметры:*
a (int) : целое положительное число (ширина прямоугольника)\
b (int) : целое положительное число (длина прямоугольника)

#### *Возвращаемое значение:*
area (int) : целое положительное число (площадь прямоугольника)

#### *Примеры вызова функции:*
area(3, 10) = 3 * 10 = 30\
area(5, 1) = 5 * 1 = 5

### *PERIMETER*
$P = (a + b) \cdot 2$

```python
def perimeter(a, b):
    return (a + b) * 2
```

#### *Параметры:*
a (int) : целое положительное число (ширина прямоугольника)\
b (int) : целое положительное число (длина прямоугольника)

#### *Возвращаемое значение:*
perimeter (int) : целое положительное число (периметр прямоугольника)

#### *Примеры вызова функции:*
perimeter(3, 25) = (3 + 25) * 2 = 56\
perimeter(32, 5) = (32 + 5) * 2 = 74


## *TRIANGLE*
### *AREA*
$S = \frac{a \cdot h}{2}$

```python
def area(a, h):
    return a * h / 2
```

#### *Параметры:*
a (int) : целое положительное число (основание треугольника)\
h (int) : целое положительное число (высота треугольника)

#### *Возвращаемое значение:*
area (float) : вещественное положительное число (площадь треугольника)

#### *Примеры вызова функции:*
area(5, 2) = 5 * 2 / 2 = 5.0\
area(6, 7) = 6 * 7 / 2 = 21.0\
area(21, 5) = 21 * 5 / 2 = 52.5

### *PERIMETER*
$P = a + b + c$

```python
def perimeter(a, b, c):
    return a + b + c
```

#### *Параметры:*
a (int) : целое положительное число (первая сторона треугольника)\
b (int) : целое положительное число (вторая сторона треугольника)\
c (int) : целое положительное число (третья сторона треугольника)

#### *Возвращаемое значение:*
perimeter (int) : целое положительное число (периметр треугольника)

#### *Примеры вызова функции:*
perimeter(66, 37, 83) = 66 + 37 + 83 = 186\
perimeter(54, 97, 18) = 54 + 97 + 18 = 169


## *CIRCLE*
### *AREA*
$S = \pi \cdot r^2$

```python
import math

def area(r):
    return math.pi * r * r
```

#### *Параметры:*
r (int) : целое положительное число (радиус круга)

#### *Возвращаемое значение:*
area (float) : вещественное положительное число (площадь круга)

#### *Примеры вызова функции:*
area(8) = $\pi \cdot 8^2$ = 201.06192982974676\
area(21) = $\pi \cdot 21^2$ = 1385.442360233099

### *PERIMETER*
$P = 2 \cdot \pi \cdot r$

```python
import math

def perimeter(r):
    return 2 * math.pi * r
```

#### *Параметры:*
r (int) : целое положительное число (радиус круга)

#### *Возвращаемое значение:*
perimeter (float) : вещественное положительное число (длина окружности круга)

#### *Примеры вызова функции:*
perimeter(10) = $2 \cdot \pi \cdot 10$ = 62.83185307179586\
perimeter(11) = $2 \cdot \pi \cdot 11$ = 69.11503837897544


# *ИСТОРИЯ ИЗМЕНЕНИЙ ПРОЕКТА*
```
* 10651b3 (HEAD -> SecondLab532471, origin/SecondLab532471) finished README.md
* 3a56981 fixed style in README.md
* 7215f22 added square and rectangle in README.md
* df9431b added comments in circle.py
* 32a60ec added comments in triangle.py
* 8be3b00 added comments in rectangle.py
* 1f5bfee added comments in square.py
* e132e0c (origin/main, origin/HEAD, new_features532471, main) created triangle.py and fixed rectangle.py
* 9648738 created rectangle.py
| * 86edb1c (origin/release) L-05: Update Docs. Add user agreement info
| * 438b89a L-05: Add user agreement
| * 6adb962 L-03: Docs added
| | * 3049431 (origin/feature) L-04: Add rectangle.py
| |/  
|/|   
| | * b5b0fae (origin/develop) L-04: Update docs for calculate.py
| | * d76db2a L-04: Add calculate.py
| | * 51c40eb L-04: Doc updated for triangle
| | * d080c78 L-04: Triangle added
| |/  
|/|   
* | d078c8d L-03: Docs added
|/  
* 8ba9aeb L-03: Circle and square added
```