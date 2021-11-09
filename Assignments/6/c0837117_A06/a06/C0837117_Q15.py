# Assignment 06
# c0837117 - Asif Mahmud
# Question 15
# Date of submission: 2021-11-09

def calc_average(score1,score2,score3,score4,score5):
    avg = round((score1+score2+score3+score4+score5)/5,2)
    return avg

def determine_grade(score):
    grade = ''
    if(score >= 90 and score <= 100):
        grade = "A"
    elif(score >= 80 and score <= 89):
        grade = "B"
    elif(score >= 70 and score <= 79):
        grade = "C"
    elif(score >= 60 and score <= 69):
        grade = "D"
    else:
        grade = "F"
    return grade

def display_result(grade1,grade2,grade3,grade4,grade5, avg):
    print("Grade for test 1: "+grade1)
    print("Grade for test 2: "+grade2)
    print("Grade for test 3: "+grade3)
    print("Grade for test 4: "+grade4)
    print("Grade for test 5: "+grade5)
    print("Average: "+str(avg))

def getScore(test):
    score = int(input("Enter score for test "+str(test)+": "))
    while(score < 0 or score > 100):
        print("Invalid input")
        score = int(input("Enter score for test "+str(test)+": "))
    return score
    
if __name__ == '__main__':
    
    score1 = getScore(1)
    score2 = getScore(2)
    score3 = getScore(3)
    score4 = getScore(4)
    score5 = getScore(5)
        
    grade1 = determine_grade(score1)
    grade2 = determine_grade(score2)
    grade3 = determine_grade(score3)
    grade4 = determine_grade(score4)
    grade5 = determine_grade(score5)
    
    avg = calc_average(score1, score2, score3, score4, score5)
    
    display_result(grade1, grade2, grade3, grade4, grade5,avg)