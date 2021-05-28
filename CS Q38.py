#Name: Yun-Ting Tsai
#Email: Yun-Ting.Tsai01@myhunter.cuny.edu
#Date: April 05,2020
#This program is to create the dayString() function.

def dayString(dayNum):
    dayString = ""
    if dayNum == 1:
        dayString = "Monday"
    elif dayNum == 2:
        dayString = "Tuesday"
    elif dayNum == 3:
        dayString = "Wednesday"
    elif dayNum == 4:
        dayString = "Thursday"
    elif dayNum == 5:
        dayString = "Friday"
    elif dayNum == 6:
        dayString = "Satursday"
    elif dayNum == 7:
        dayString = "Sunday"
    return(dayString)


def main():
    n = int(input('Enter the number of the day: '))
    dString = dayString(n)
    print('The day is', dString + ".")


if __name__ == "__main__":
    main()
