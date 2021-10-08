# Assignment 04
# c0837117 - Asif Mahmud
# Question 03
# Date of submission: 2021-10-08

if __name__ == '__main__':
    budget = float(input("Enter budget amount: "))
    total_expense = 0
    while 1==1:
        new_amount = float(input("Enter new expense or press 0 to calculate total amount:"))
        if(new_amount == 0):
            break
        else:
            total_expense += new_amount
            
    print("Budget: "+ str(budget))
    print("Calculated expense: "+str(total_expense))
    if(total_expense > budget):
        print("You're total expense is over budget")
    else:
        print("You're total expense is under budget")