#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: ,2020
#This program is to draw the shades of red. 

import turtle			   

turtle.colormode(255)           #Must set the range of colors. Otherwise, Python cannot recognize.
tess = turtle.Turtle()		
tess.shape("turtle")
tess.backward(100)

for i in range(0,255,10):
     tess.forward(10)
     tess.pensize(i)		#Set the drawing size to be i (larger each time)
     tess.color(i,0,i)          #Because the start color is black, color will get brighter.
