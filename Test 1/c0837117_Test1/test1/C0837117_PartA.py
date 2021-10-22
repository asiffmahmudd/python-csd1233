# Test 01
# c0837117 - Asif Mahmud
# Part A
# Date of submission: 2021-10-22

from math import sqrt

if __name__ == '__main__':
    max_marks = -1
    min_marks = 999999
    sum_of_marks = 0
    student_exists = 'Y'
    count = 0
    
    while(student_exists == 'Y'):
        student_exists = input("Do you have another student to enter [Y/N]? ")
        if(student_exists != 'Y'):
            break
        else:
            marks = float(input("Enter Student "+str(count+1)+"'s final percentage grade: "))
            while(marks < 0 or marks > 100):
                print("Please enter a percentage in the range 0-100")
                marks = float(input("Enter Student "+str(count+1)+"'s final percentage grade: "))
            sum_of_marks += marks
            if(min_marks > marks):
                min_marks = round(marks,1)
            if(max_marks < marks):
                max_marks = round(marks,1)
            count += 1
    
    avg = round(sum_of_marks/count,1)
    
    print("************************************************")
    
    sd_input = input("Would you like to include standard deviation in your summary statistics [Y/N]? ")
    sd = 0
    if(sd_input == 'Y'):
        print("Please re-enter the same percentage grades as you previously did for each student")
        sum_of_marks = 0
        for i in range(count):
            marks = float(input("Student "+str(i+1)+": "))
            sum_of_marks += ((marks-avg)*(marks-avg))
        
        sd = round(sqrt(sum_of_marks/count),2)
    print("************************************************")
    
    print("MAX: "+str(max_marks)+"%")
    print("MIN: "+str(min_marks)+"%")
    print("AVG: "+str(avg)+"%")
    
    if(sd_input == 'Y'):
        print("SD: "+str(sd))