#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: March 16,2020
#This program is to draw a borough graph.

import matplotlib.pyplot as plt

import pandas as pd

data = input("Where is your borough? ")
newname = input("What is your output file name? ")

pop = pd.read_csv('nycHistPop.csv', skiprows=5)
#skiprows: In the data, the first five rows do not have anything,so we should skip these lines to analysis the data.

print(pop)

pop["Fraction"] = pop[data]/pop["Total"]

pop.plot(x="Year", y="Fraction Single")

fig = plt.gcf()

plt.show()

fig.savefig(newname)
