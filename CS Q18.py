#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: 03.04.2020
#This program is to count the number of coins.

cents = int(input("How many cents you have as an integer? "))

quarters = cents // 25
rem = cents % 25

if quarters > 0:
    print("Quarters:", str(quarters))
else:
    print("Quarters:", 0)
    
if rem > 0:
    dimes = rem // 10
    rem = rem % 10
    nickels = rem // 5
    cents = rem % 5
    print("Dimes:", dimes)
    print("Nickels:", nickels)
    print("Cents:", cents)
else:
    print("Dimes:", 0)
    print("Nickels:", 0)
    print("Cents:", 0)
