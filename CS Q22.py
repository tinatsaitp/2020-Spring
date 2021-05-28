#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: 03.10.2020
#This program is to create a line spiral.

import turtle
Tina = turtle.Turtle()

turn = int(input("How many turns do you want to put in? "))

for i in range(0, turn, 2):
    Tina.forward(i)
    Tina.right(45)
