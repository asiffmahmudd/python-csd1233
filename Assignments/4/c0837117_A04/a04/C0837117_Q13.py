# Assignment 04
# c0837117 - Asif Mahmud
# Question 13
# Date of submission: 2021-10-08

if __name__ == '__main__':
    starting_number = int(input("Starting number of organisms: "))
    daily_increase = float(input("Average daily increase: "))
    days = int(input("Number of days to multiply: "))
    
    i = 2
    print("Day Approximate \t Population")
    print("1 \t\t\t " + str(starting_number))
    
    while(i <= days):
        current_num = starting_number + (daily_increase/100)*starting_number
        print(str(i) + " \t\t\t " + str(current_num))
        i += 1
        starting_number = current_num