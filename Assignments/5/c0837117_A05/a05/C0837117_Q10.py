# Assignment 05
# c0837117 - Asif Mahmud
# Question 10
# Date of submission: 2021-11-04

def calculateAndDisplay(currentTuition, tuitionIncrement, years):
    for i in range(1,years+1):
        tuition = round(currentTuition+currentTuition*tuitionIncrement, 2)
        print("Tuition in the next " + str(i) + " years: " + str(tuition))
        currentTuition = tuition
    
if __name__ == '__main__':
    currentTuition = 8000
    tuitionIncrement = 3/100
    years = 5
    calculateAndDisplay(currentTuition, tuitionIncrement, years)