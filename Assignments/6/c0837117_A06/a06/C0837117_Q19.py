# Assignment 06
# c0837117 - Asif Mahmud
# Question 19
# Date of submission: 2021-11-09

def getInput():
    presentValue = float(input("Enter present value of the account: "))
    while(presentValue < 0):
        print("invalid input")
        presentValue = float(input("Enter present value of the account: "))
        
    interestRate = float(input("Enter monthly interest rate: "))
    while(interestRate < 0 or interestRate > 30):
        print("invalid input")
        interestRate = float(input("Enter monthly interest rate: "))
    
    numberOfMonths = int(input("Enter number of months: "))
    while(numberOfMonths <= 0):
        print("invalid input")
        numberOfMonths = int(input("Enter number of months: "))
        
    return presentValue, interestRate, numberOfMonths
 
def calculateFutureValue(presentValue, interestRate, numberOfMonths):
    futureValue = presentValue*pow((1+(interestRate/100)), numberOfMonths)
    return futureValue
    
if __name__ == '__main__':
    
    presentValue, interestRate, numberOfMonths = getInput()
    futureValue = calculateFutureValue(presentValue, interestRate, numberOfMonths)
    
    print("The account's future value is: "+str(round(futureValue,2)))
    