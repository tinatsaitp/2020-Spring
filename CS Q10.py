#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: ,2020
#This program is to do GC Content.

mess = "AAAAA"
l = len(mess)
print("The length is", l)

numC = mess.count('C')
numG = mess.count('G')

gc = (numC+numG)/ 1
print("GC-content is", gc)

if gc == 0:
    print("First G found at position", -1)
    print("First C found at position", -1)
else:
    G = mess.index('G')
    print("First G found at position", G)
    
    C = mess.index('C')
    print("First C found at position", C)



mess = "ACGCCCGGGATG"
l = len(mess)
print("The length is", l)

numC = mess.count('C')
numG = mess.count('G')

gc = (numC + numG) / l
print("GC-content is", gc)

G = mess.index('G')
print("First G found at position", G)

C = mess.index('C')
print("First C found at position", C)
