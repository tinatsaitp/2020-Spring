#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: March 24,2020
#This program is to create a shelter census with plot chart.

import matplotlib.pyplot as plt
import pandas as pd

data = input("What is your file? ")
newname = input("What is your output file name? ")

homeless = pd.read_csv(data)


homeless["Fraction Single"] = homeless["Total Single Adults in Shelter"]/homeless["Total Individuals in Shelter"]

homeless.plot(x="Date of Census", y="Fraction Single")

fig = plt.gcf()

plt.show()

fig.savefig(newname)
