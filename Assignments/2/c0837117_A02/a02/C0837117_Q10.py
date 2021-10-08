# Assignment 02
# c0837117 - Asif Mahmud
# Question 10
# Date of submission: 2021-09-25

if __name__ == '__main__':
    num_of_cookies = 48
    cup_of_butter = 1
    cup_of_flour = 2.75
    cup_of_sugar = 1.5
    num_of_cookies_demanded = cup_of_butter_needed = cup_of_flour_needed = cup_of_sugar_needed = 0
    
    num_of_cookies_demanded = int(input("How many cookies you want to make?"))
    cup_of_butter_needed = num_of_cookies_demanded*cup_of_butter/num_of_cookies
    cup_of_flour_needed = num_of_cookies_demanded*cup_of_flour/num_of_cookies
    cup_of_sugar_needed = num_of_cookies_demanded*cup_of_sugar/num_of_cookies
    
    print("Cup of butter needed: "+ str("{:.2f}".format(cup_of_butter_needed)))
    print("Cup of flour needed: "+ str("{:.2f}".format(cup_of_flour_needed)))
    print("Cup of sugar needed: "+ str("{:.2f}".format(cup_of_sugar_needed)))
    