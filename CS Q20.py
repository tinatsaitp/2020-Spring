#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: 03.06.2020
#This program is to create a image with blue stripes.

num = int(input("What is the size of your imaage? "))
outputname = input("What is the name of your output file? ")

import matplotlib.pyplot as plt
import numpy as np

img = np.ones((num,num,3))

img[ : , : :2,0:2] = 0

plt.imshow(img)
plt.show()

plt.imsave(outputname, img)
