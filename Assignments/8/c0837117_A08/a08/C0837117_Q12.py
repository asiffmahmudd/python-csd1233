# Assignment 08
# c0837117 - Asif Mahmud
# Question 12
# Date of submission: 2021-11-29

#checking if the number is prime or not
def is_prime(num):
    f = 0
    for divisor in range(2, num):
        if(num % divisor == 0):
            f = 1
            break
    if f == 0:
        print(str(num)+" is a prime number")
    else:
        print(str(num)+" is not a prime number")

#getting input from the user
def get_input():
    userInput = ""
    try:
        userInput = int(input("Enter an integer greater than 1: "))
    except:
        print("Invalid input! Please try again.")
    while not isinstance(userInput, int) or userInput <= 1:
        try:
            userInput = int(input("Enter an integer greater than 1: "))
        except:
            print("Invalid input! Please try again.")
        else:
            if userInput <= 1:
                print("Invalid input! Please try again.")
        
    return userInput
    
if __name__ == '__main__':
    userInput = get_input()
    
    numList = []
    for num in range(2, userInput+1):
        numList.append(num)
    
    for num in numList:
        is_prime(num)