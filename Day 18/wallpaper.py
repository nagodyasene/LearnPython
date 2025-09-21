from logging import currentframe
from turtle import Turtle, Screen

s = Screen()
cursor = Turtle()
cursor2 = Turtle()

cursor.speed(100)
cursor2.speed(1000)

while True:
    cursor.forward(200)
    cursor.left(170)
    if abs(cursor.pos()) < 1:
        break

cursor.hideturtle()

cursor2.teleport(240)
cursor2.left(90)


for _ in range(360):
    cursor2.left(1)
    cursor2.fd(0.41 * 6)

cursor2.hideturtle()

s.exitonclick()