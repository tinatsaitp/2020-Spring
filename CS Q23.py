#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: 03.11.2020
#This program is to count the amount of snow.

import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("CaliforniaDrought_02232014_md.png")
countShow = 0
t = 0.75

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if (img[i,j,0] > t) and (img[i,j,1] > t) and (img[i,j,2] > t):
            countShow += 1

print("snow count of", countShow)



img = plt.imread("CaliforniaDrought_02122013_md.png")
countShow = 0
t = 0.75

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if (img[i,j,0] > t) and (img[i,j,1] > t) and (img[i,j,2] > t):
            countShow += 1

print("snow count of", countShow)



img = plt.imread("CaliforniaDrought_02232011_md.png")
countShow = 0
t = 0.75

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if (img[i,j,0] > t) and (img[i,j,1] > t) and (img[i,j,2] > t):
            countShow += 1

print("snow count of", countShow)
