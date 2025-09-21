import random
from turtle import Turtle, Screen

tim = Turtle()
tim.hideturtle()

screen = Screen()
screen.colormode(255)

tim.speed(0)

def random_pen_color():
    tim.pencolor((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255)))

def draw_circle():
    random_pen_color()
    for _ in range(360):
        tim.right(1)
        tim.forward(1.745329252)

def stenograph():
    while tim.heading() != 10.0:
        tim.right(10)
        draw_circle()

stenograph()