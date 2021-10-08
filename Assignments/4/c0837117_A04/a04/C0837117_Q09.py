# Assignment 04
# c0837117 - Asif Mahmud
# Question 09
# Date of submission: 2021-10-08


if __name__ == '__main__':
    current_year = 2021
    year = current_year
    rising_rate = 1.6
    height = 0
    while(year <= current_year + 25):
        height += rising_rate
        year += 1
        print(str(year) + ": " + str("{:.2f}".format(height)) + "mm")