# площадь круга.

radius = float(input("radius circle: "))
area = 3.14 * radius ** 2
print("radius circle is ", area)


# квадрат на экране.

import turtle

t = turtle.Turtle()

t.begin_fill()
for i in range(12):
    t.forward(int(radius))
    t.left(int(radius)+10)
t.end_fill()

turtle.done()56


