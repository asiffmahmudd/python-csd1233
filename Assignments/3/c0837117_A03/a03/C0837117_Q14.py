# Assignment 03
# c0837117 - Asif Mahmud
# Question 14
# Date of submission: 2021-09-30

if __name__ == '__main__':
    height = float(input("Enter your height: "))
    weight = float(input("Enter your weight: "))
    
    bmi = weight*703/height**2
    
    print("Your BMI: "+str(round(bmi, 2)))
    
    if(bmi >= 18.5 and bmi <= 25):
        print("Your weight is optimal.")
    elif(bmi < 18.5):
        print("You are underweight.")
    elif(bmi > 25):
        print("You are overweight.")