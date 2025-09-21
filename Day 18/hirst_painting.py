# import colorgram
#
# colors = colorgram.extract("painting.jpg", 30)
#
# color_list = []
# for x in range(len(colors)):
#     red = colors[x].rgb.r
#     green = colors[x].rgb.g
#     blue = colors[x].rgb.b
#     rgb_tuple = (red,green,blue)
#     color_list.append(rgb_tuple)
#
# print(color_list)

import random as r
from turtle import Turtle as T, Screen
from turtle import Screen as S

screen = S()
tim = T()

tim.speed("fastest")
tim.hideturtle()
screen.colormode(255)

data = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]

def random_color():
    color = r.choice(data)
    tim.pencolor(color)
    tim.fillcolor(color)

def draw_circle():
    random_color()
    tim.begin_fill()
    tim.dot(20)
    tim.end_fill()
    tim.penup()
    tim.teleport(tim.pos()[0] + 50)

def upper_row():
    pos_x , pos_y = tim.pos()
    tim.teleport(0, pos_y + 50)

# 50 yukarı çıkacak

for row in range(10):
    for column in range(10):
        draw_circle()
    upper_row()

screen.exitonclick()