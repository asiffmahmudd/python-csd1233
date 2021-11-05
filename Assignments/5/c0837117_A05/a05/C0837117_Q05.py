# Assignment 05
# c0837117 - Asif Mahmud
# Question 05
# Date of submission: 2021-11-04

def getYear():
    years = int(input("Enter the number of years: "))
    while(years < 0):
        print("Invalid input for year")
        years = int(input("Enter the number of years: "))
    return years

def getTotalRainfall(years):
    totalRainfall = 0
    for i in range(1, years+1):
        for j in range(1, 13):
            rainfall = float(input("Enter inches of rainfall for year " + str(i) + " month " + str(j) + ": "))
            while(rainfall < 0):
                print("Invalid input for rainfall")
                rainfall = float(input("Enter inches of rainfall for year " + str(i) + " month " + str(j) + ": "))
            totalRainfall += rainfall
    return totalRainfall
 
def displayResult(years, totalRainfall):
   print("Number of months: "+str(years*12))
   print("Total rainfall: "+str(totalRainfall))
   print("Average rainfall per month: "+ str(totalRainfall/(years*12)))
   
if __name__ == '__main__':
    years = getYear()
    totalRainfall = getTotalRainfall(years)
    displayResult(years, totalRainfall)
    
    