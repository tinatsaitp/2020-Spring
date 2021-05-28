#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: April 04,2020
#This program is to create a daily absence data with plot chart.

import matplotlib.pyplot as plt
import pandas as pd

data = input("Enter name of input file: ")
newname = input("Enter name of output file: ")

dailyabsence = pd.read_csv(data)

df = pd.DataFrame(dailyabsence)


df["Date"] = pd.to_datetime(df["Date"].apply(str))

df["% Absent"] = df["Absent"]/df["Enrolled"]*100

dailyabsence.plot(x="Date", y="% Absent")

fig = plt.gcf()

plt.show()

fig.savefig(newname)
