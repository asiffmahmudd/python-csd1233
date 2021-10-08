# Assignment 03
# c0837117 - Asif Mahmud
# Question 16
# Date of submission: 2021-09-30

if __name__ == '__main__':
    year = int(input("Enter year: "))
    
    if(year % 100 == 0 and year % 400 == 0):
        print("In " + str(year) + " February has 29 days")
    elif(year % 100 != 0 and year % 4 == 0):
        print("In " + str(year) + " February has 29 days")
    else:
        print("In " + str(year) + " February has 28 days")