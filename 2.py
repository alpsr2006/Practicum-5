import math, turtle as t
xc = int(input(': '))
yc = int(input(': '))
r = int(input(': '))
x = int(input(': '))
y = int(input(': '))
#Вычисление расстояния от центра до точки
d = math.sqrt((xc - x) ** 2 + (yc - y) ** 2)
q = 0
if d < r:
    q = "Точка внутри окружности"
elif d > r:
    q = "Точка вне окружности"
else:
    q = "Точка на окружности"
t.speed(5)
t.penup()
t.goto(xc, yc-r)
t.pendown()
t.circle(r)
t.penup()
t.goto(x, y)
t.dot(5)
t.hideturtle()
t.goto(-60,-130)
t.write(q)
t.done()

