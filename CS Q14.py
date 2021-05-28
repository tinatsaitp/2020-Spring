#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: 02.27.2020
#This program is to draw a "U"niversity logo.

import matplotlib.pyplot as plt
import numpy as np

img = np.ones((30,30,3))

img[ : , :10,1:3] = 0
img[ : ,20: ,1:3] = 0
img[20: , : ,1:3] = 0

plt.imshow(img)
plt.show()

plt.imsave("logo.png", img)
