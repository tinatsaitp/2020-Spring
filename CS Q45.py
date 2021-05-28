#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: April 25,2020
#This program is to create a map which locates at Hunter College via Folium. 

import folium

HunterMap = folium.Map(location = [40.75, -74.125], zoom_start=10)

name = "Hunter College"
lat, lon = 40.768731, -73.964915

newMark = folium.Marker([lat, lon], popup=name)
newMark.add_to(HunterMap)

HunterMap.save(outfile = "nycMap.html")
