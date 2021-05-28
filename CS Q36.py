#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: April 04,2020
#This program is to create a film permits data.

import pandas as pd

inF = input("Enter file name: ")
filmpermits = pd.read_csv(inF)

totalpermits = filmpermits["Borough"].count()
print("There were", totalpermits,"film permits.")
print(filmpermits["Borough"].value_counts())

print("The five most popular filming locations were")
print(filmpermits["ParkingHeld"].value_counts()[ :5])
