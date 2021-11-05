# Assignment 05
# c0837117 - Asif Mahmud
# Question 08
# Date of submission: 2021-11-04

def getResult():
    num = 0
    sum = 0
    while num >= 0:
        num = int(input("Enter positive number for the series and negative number to end the series: "))
        if(num > 0):
            sum += num
    return sum
        
if __name__ == '__main__':
    sum = getResult()
    print("The sum of the series is: "+str(sum))