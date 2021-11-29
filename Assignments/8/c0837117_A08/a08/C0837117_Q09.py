# Assignment 08
# c0837117 - Asif Mahmud
# Question 09
# Date of submission: 2021-11-29

#reading the file
def read_file(file):
    populations = []
    for line in file:
        record = int(line.rstrip())
        populations.append(record)
    return populations    

#calculating maximum year, minimum year and average change
def calculate_result(populations):
    year = 1951
    avgChange = 0
    listLen = len(populations) 
    maxIncrease = 0
    minIncrease = 9999999999
    minYear = 0
    maxYear = 0
    if(listLen > 1):
        sum = 0
        for i in range(1, listLen):
            diff = abs(populations[i]-populations[i-1])
            sum += diff
            if diff > maxIncrease:
                maxIncrease = diff
                maxYear = year+i
            elif diff < minIncrease:
                minIncrease = diff
                minYear = year+i
        avgChange = sum/listLen
    else:
        avgChange = abs(populations[0]-populations[1])/2
        if populations[0] > populations[1]:
            maxYear = year+1
            minYear = year
        else:
            maxYear = year
            minYear = year+1
    
    return round(avgChange,2), minYear, maxYear

if __name__ == '__main__':
    fp_population = open("data/USPopulation.txt")
    populations = read_file(fp_population)
    avgChange, minYear, maxYear = calculate_result(populations)
    print("Average annual change in population: "+str(avgChange))
    print("Year with biggest increase in population: "+str(minYear))
    print("Year with smallest increase in population: "+str(maxYear))