#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: April 25,2020
#This program is to make a collisions map.

import pandas as pd
import folium

inFile = input("Enter your file: ")
outFile = input("Enter the output name: ")

inF = pd.read_csv(inFile)

trafficMap = folium.Map(location=[40.75, -73.964915])

for index, row in inF.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup = name)
    newMarker.add_to(trafficMap)

trafficMap.save(outfile = outFile)
