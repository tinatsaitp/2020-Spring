#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: March 16,2020
#This program is to draw a borough stats.

import matplotlib.pyplot as plt

import pandas as pd

place = input("Where is your borough? ")

pop = pd.read_csv('nycHistPop.csv', skiprows=5)
#skiprows: In the data, the first five rows do not have anything,so we should skip these lines to analysis the data.

print(pop)

print("The minimum population is", pop[place].min())
print("The maximum population is", pop[place].max())
print("The average population is", pop[place].mean())
print("The standard deviation is", pop[place].std())
