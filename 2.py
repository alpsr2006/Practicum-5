import math
xc = int(input(': '))
yc = int(input(': '))
r = int(input(': '))
x = int(input(': '))
y = int(input(': '))
r_xy = math.sqrt(x ** 2 + y ** 2)
if r_xy <= r:
    print("Точка внутри окружности")
else:
    print("Точка вне окружности")
