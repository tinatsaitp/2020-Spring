#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: 02.26.2020
#This program is to change the Image's color.

import matplotlib.pyplot as plt
import numpy as np


img = plt.imread('csBridge.png')
plt.imshow(img)
plt.show()

img2 = img.copy()
img2[:,:,0] = 0          
img2[:,:,2] = 0

plt.imshow(img2)
plt.show()

plt.imsave('out1.png', img2)



img3 = plt.imread('acTree.png')
plt.imshow(img3)
plt.show()

img4 = img3.copy()
img4[:,:,0] = 0          
img4[:,:,2] = 0

plt.imshow(img4)
plt.show()

plt.imsave('out2.png', img4)
