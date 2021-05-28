#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: ,2020
#This program is to make a pink screen.

import turtle
wn = turtle.Screen()             
wn.bgcolor("pink")


tess = turtle.Turtle()           
tess.color("blue")
tess.pensize(5)

alex = turtle.Turtle()           

tess.forward(80)                 
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                  

tess.right(180)                 
tess.forward(80)

alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()
