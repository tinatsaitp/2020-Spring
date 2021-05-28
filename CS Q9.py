#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: ,2020
#This program is to encrypt message.

mess = input("What does the word you want to put in?" )
k = 16
cipher = ""
newcipher = ""

for i in range(len(mess)):
    num = ord(mess[i])
    newnum = num+k
    if newnum <= 122:
        cipher = chr(newnum)
    elif newnum > 122:
        cipher = chr(newnum-26)
    newcipher = newcipher + cipher
print("The new coded message is", newcipher)
