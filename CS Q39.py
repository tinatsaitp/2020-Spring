#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: April 05,2020
#This program is to make a AMNH admission price calculator.

def computePrice(ageGroup, ticketType):
    price = 0
    if ticketType == "admission" and ageGroup == "adult":
        price = "23"
    elif ticketType == "admission" and ageGroup == "child":
        price = "13"
    elif ticketType == "admission" and ageGroup == "senior":
        price = "18"
    elif ticketType == "+exhibitions" and ageGroup == "adult":
        price = "33"
    elif ticketType == "+exhibitions" and ageGroup == "child":
        price = "20"
    elif ticketType == "+exhibitions" and ageGroup == "senior":
        price = "27"
    else:
        return(-1)
    return(price)

def main():
     a = input('Enter the age group (child, adult, senior): ')
     t = input('Enter the ticket type (admission / +exhibitions): ').lower()
     price = computePrice(a,t)
     print('The price of your ticket is', price)

if __name__ == "__main__":
     main()
