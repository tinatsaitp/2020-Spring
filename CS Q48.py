#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: April 26,2020
#This program is to do error checking.

num = 0
total = 0
count = 0
average = 0
while average < 50:
    num = int(input("Please enter number: "))
    total = total + num
    count = count + 1
    average = total/count

print("The average is", average)
