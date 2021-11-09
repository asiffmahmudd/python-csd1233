# Assignment 06
# c0837117 - Asif Mahmud
# Question 08
# Date of submission: 2021-11-09

from math import ceil

def validateInput(value, type):
    while value <= 0:
        print("Invalid input")
        if(type == 1):
            value = float(input("Enter wall space in square feet: "))
        else:
            value = float(input("Enter paint price per gallon: "))
    return value

def getInput():
    wallSpace = float(input("Enter wall space in square feet: "))
    wallSpace = validateInput(wallSpace, 1)
    paintPrice = float(input("Enter paint price per gallon: "))
    paintPrice = validateInput(paintPrice, 2)
    
    return wallSpace, paintPrice

def calculateAndDisplay(wallSpace, paintPrice):
    numberOfGallons = ceil(wallSpace/112)
    hoursOfLabor = round((8*wallSpace)/112,2)
    costOfPaint = round(numberOfGallons*paintPrice,2)
    laborCharge = round(hoursOfLabor*35.00,2)
    totalCost = round(laborCharge+costOfPaint,2)
    
    print("Number of gallons of paint required: "+str(numberOfGallons))
    print("Hours of labor required: "+str(hoursOfLabor))
    print("Cost of the paint: "+str(costOfPaint))
    print("Labor charges: "+str(laborCharge))
    print("Total cost: "+str(totalCost))
   
if __name__ == '__main__':
    wallSpace, paintPrice = getInput()
    calculateAndDisplay(wallSpace, paintPrice)
    