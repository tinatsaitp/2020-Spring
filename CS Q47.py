#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: April 25,2020
#This program is to make a picture with random walk.

import turtle
import random

tina = turtle.Turtle()
tina.speed(20)

for i in range(100):
    tina.forward(20)
    a = random.randrange(0,360,5)
    tina.left(a)
