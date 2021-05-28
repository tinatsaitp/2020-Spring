#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: March 08,2020
#This program is to create a topo map.

import numpy as np
import matplotlib.pyplot as plt

colorofdegree = float(input("What is your amount of bule? "))

newname = input("What does your new file's name? ")

elevations = np.loadtxt('elevationsNYC.txt')

mapShape = elevations.shape + (3,)

topoMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= -10:
           topoMap[row,col,0:3] = 0.2

        elif elevations[row,col] <= 0:
           topoMap[row,col,2] = colorofdegree
           
        elif elevations[row,col] % 10 == 0:
           topoMap[row,col,0:3] = 0.0
           
        else:
            topoMap[row,col,0:3] = 1.0

plt.imshow(topoMap)

plt.show()

plt.imsave(newname, topoMap)

print("Thank you for using my program!")
print("Your map is stored", newname + ".")
