name = input("Как вас зовут? ")
print("Привет,", name, "!")

# площадь круга.

radius = float(input("Введите радиус круга: "))
area = 3.14 * radius ** 2
print("Площадь круга равна", area)


# квадрат на экране.

import turtle

t = turtle.Turtle()

t.begin_fill()
for i in range(12):
    t.forward(200)
    t.left(210)
t.end_fill()

turtle.done()


