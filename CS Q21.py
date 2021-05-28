#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: 03.09.2020
#This program is to organize a list of names.

namelist = input("What are your name lists? ")

sep = namelist.split(", ")

finalnl = ''

for i in sep:
    sepname = i.split(' ')
    lastname = sepname[1]
    newlast = lastname[0]
    finalnl = newlast + '. ' + sepname[0]
    print(finalnl)



