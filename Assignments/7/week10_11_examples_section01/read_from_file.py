
if __name__ == '__main__':
    
    sum_of_grades = 0
    num_of_students = 0
    course_avg = 0
    
    #STEP 01: OPEN the file
    fp = open("Student_Grades.txt", 'r') #opens file for READing
    
    #STEP 02: PROCESSING the file
    #file_contents = fp.read()
    
    # line = fp.readline()
    # while line != '': 
    #     line = line.rstrip()
    #     print(line)
    #     line = fp.readline()
        
    for line in fp:
        record = line.rstrip()
        fields = record.split(",")
        sum_of_grades += float(fields[2])
        num_of_students += 1
    
    #Step 03: CLOSE the file
    fp.close()
    
    course_avg = sum_of_grades / num_of_students
    
    print("The course average is", course_avg, "%")
 