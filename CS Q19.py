#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: 03.05.2020
#This program is to make a turtle spiral.

mess = int(input("How many number of stemps? "))

import turtle

tina = turtle.Turtle()

tina.shape("turtle")

tina.penup()
step = int(20)
    
for i in range(mess+1):
    step = step + int(2)
    tina.forward(step)
    tina.right(24)
    tina.stamp( )
    print(i)
