# Assignment 05
# c0837117 - Asif Mahmud
# Question 12
# Date of submission: 2021-11-04

def getInput():
    num = int(input("Enter a positive integer: "))
    while(num <= 0):
        print("Invalid input")
        num = int(input("Enter a positive integer: "))
    return num

def getFactorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    return factorial

if __name__ == '__main__':
    num = getInput()
    factorial = getFactorial(num)
    print("Factorial of " + str(num) + ": " + str(factorial))