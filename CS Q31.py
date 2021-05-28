#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: March 24,2020
#This program is to make a turtle string.

import turtle

tina = turtle.Turtle()

mess = input("What is your comand string? ")

for ch in mess:
    if ch == 'F':
        tina.forward(50)
    elif ch == 'B':
        tina.backward(50)
    elif ch == 'L':
        tina.left(90)
    elif ch == 'R':
        tina.right(90)
    elif ch == 'S':
        tina.shape("turtle")
        tina.stamp()
    elif ch == 'D':
        tina.dot()
    elif ch == '^':
        tina.penup()
    elif ch == 'v':
        tina.pendown()
    elif ch == 'r':
        tina.color("red")
    elif ch == 'g':
        tina.color("green")
    elif ch == 'b':
        tina.color("blue")
    elif ch == 'p':
        tina.color("purple")
    else:
        print("Error: do not know the command:", ch)
