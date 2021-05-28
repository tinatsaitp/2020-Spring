#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: March 24,2020
#This program is to create a stars data.

import pandas as pd

filename = input("Enter file name: ")
startype = input("Enter the name of the star type: ")

stars = pd.read_csv(filename)

print("The radius of the largest", startype, "is", stars.groupby(['Star type']).get_group(startype).max()['Radius(R/Ro)'])
print("The radius of the smallest", startype, "is", stars.groupby(['Star type']).get_group(startype).min()['Radius(R/Ro)'])
