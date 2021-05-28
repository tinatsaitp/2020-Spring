#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: April 04,2020
#This program is to create a character counter.

code = input("Please enter a codeword: ")

uppercount = 0
lowercount = 0
numcount = 0
specialcount = 0

for wd in code:
    if 90 >= ord(wd)>= 65:
        uppercount = uppercount + 1
    elif 122 >= ord(wd)>= 97:
        lowercount = lowercount + 1
    elif 57 >= ord(wd)>= 48:
        numcount = numcount + 1
    else:
        specialcount = specialcount + 1

print("Your codeword contains", uppercount, "uppercase letters,", lowercount, "lowercase letters,", numcount, "numbers,",  "and", specialcount, "special characters.")
