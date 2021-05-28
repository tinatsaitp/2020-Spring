#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: April 04,2020
#This program is to draw turtle triangles.

import turtle
def setUp(t, dist):
    t.penup()
    t.forward(dist)
    t.pendown()

def triangle(t, length):    
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
        triangle(t, length/2)

def nestedTriangle(t, length):
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
            triangle(t, length/2)

def main():
    n = int(input('Enter length: '))

    tom = turtle.Turtle()
    setUp(tom, -100)
    triangle(tom, n)

    tess = turtle.Turtle()
    setUp(tess, 100)
    nestedTriangle(tess, n)

if __name__ == "__main__":
     main()
