# Assignment 02
# c0837117 - Asif Mahmud
# Question 14
# Date of submission: 2021-09-25

if __name__ == '__main__':
    P = r = A = 0.0
    n = t = 0
    
    P = float(input("Enter the amount of principal originally deposited into the account: "))
    r = float(input("Enter the annual interest rate paid by the account: "))
    r = r/100
    n = int(input("Enter the number of times per year that the interest is compounded: "))
    t = int(input("Enter the number of years the account will be left to earn interest: "))
    
    A = P*(1+(r/n))**(n*t)
    
    print("The amount of money that will be in the account after "+str(t)+" years: "+str("{:.2f}".format(A)))