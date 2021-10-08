# Assignment 03
# c0837117 - Asif Mahmud
# Question 09
# Date of submission: 2021-09-30

if __name__ == '__main__':
    pocket_number = int(input("Enter a pocket number: "))
    
    if(pocket_number == 0):
        print("Green")
    elif(pocket_number >= 1 and pocket_number <= 10) or (pocket_number >= 19 and pocket_number <= 28):
        if(pocket_number % 2 == 0):
            print("Black")
        else:
            print("Red")
    elif(pocket_number >= 11 and pocket_number <= 18) or (pocket_number >= 29 and pocket_number <= 36):
        if(pocket_number % 2 == 0):
            print("Red")
        else:
            print("Black")
    else:
        print("Invalid Number!")