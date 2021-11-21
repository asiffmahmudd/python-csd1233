# Assignment 07
# c0837117 - Asif Mahmud
# Question 01
# Date of submission: 2021-11-21

#displaying menu
def display_menu():
    print("MENU:")
    print(" (D)elete a record")
    print(" (I)nsert a record")
    print(" (F)ind matching records")
    print(" (S)tatistical data")
    print(" (E)xit")
    
def get_menu_selection():
    display_menu()
    
    selection = input("Please enter your choice:").upper()
    
    while selection not in ['D', 'I', 'F', 'S', 'E']:
        print("ERROR: Invalid menu selection. Please try again!\n")
        display_menu()
        selection = input("Please enter your choice:").upper()
    
    return selection

#Use this function to pass in first or last name and convert first letter to upper
#and remaining characters to lower BEFORE inserting, searching, deleting from file
def get_proper_case_name(name):
    correct_case_name = ""
    for ch in range(0, len(name)):
        if ch == 0:
            correct_case_name = name[ch].upper()
        else:
            correct_case_name += name[ch].lower()
    
    return correct_case_name

#Copies the contents from scratch.csv file to grades.csv
def copy_scratch():
    
    fp_scratch = open("data/scratch.csv", "r")
    fp_grades = open("data/grades.csv", "w")
    
    for record in fp_scratch:
        fp_grades.write(record)
        
    fp_scratch.close()
    fp_grades.close()


def delete_record(first, last):
    record = ""
    fp_grades = open("data/grades.csv", "r")
    fp_scratch = open("data/scratch.csv", "w")
    deleted = 0
    for line in fp_grades:
        record = line.rstrip()
        fields = record.split(",")
        
        if(deleted == 0 and fields[1] == first and fields[0] == last):
            deleted = 1
        else:
            #tell method allows us byte offset where the file pointer is
            if fp_scratch.tell() != 0: 
                record = "\n" + record
            fp_scratch.write(record)
            
    fp_grades.close()
    fp_scratch.close()

    if deleted == 1:
        copy_scratch()
    print("\nSuccessfully deleted record, if one existed!")
    # else:
    #     print("\nStudent record not found")
  
#inserts a particular line in the scratch file      
def insert_line(fp_scratch, adding_line):
    if fp_scratch.tell() != 0:
        adding_line = "\n"+adding_line
    elif fp_scratch.tell() == 0:
        adding_line += "\n"
    fp_scratch.write(adding_line)
    print("\nRecord inserted successfully")

def insert_record(first, last, grade):
    adding_line = last + "," + first + "," + str(grade)
    record = ""
    fp_grades = open("data/grades.csv", "r")
    fp_scratch = open("data/scratch.csv", "w")
    inserted = 0
    for line in fp_grades:
        record = line.rstrip()
        fields = record.split(",")
        
        #tell method allows us byte offset where the file pointer is
        if fp_scratch.tell() != 0: 
            record = "\n" + record
        
        if inserted == 0:
            if last < fields[0]:
                insert_line(fp_scratch, adding_line)
                inserted = 1
            elif last == fields[0]:
                if first < fields[1]:
                    insert_line(fp_scratch, adding_line)
                    inserted = 1
                elif first == fields[1] and grade <= int(fields[2]):
                    insert_line(fp_scratch, adding_line)
                    inserted = 1
        fp_scratch.write(record)
        
    if inserted == 0:
        fp_scratch.write("\n"+adding_line)
        print("\nRecord successfully inserted: "+last+","+first+","+grade)
       
    fp_grades.close()
    fp_scratch.close()

def find_record(first, last):
    fp_grades = open("data/grades.csv", "r")
    found = 0
    for line in fp_grades:
        record = line.rstrip()
        fields = record.split(",")
        if(first == fields[1] and last == fields[0]):
            found += 1
            if found == 1:
                print("\nMatching record(s):")
            print(fields[1] + ","+ fields[0] + ","+ fields[2])
    print("")        
    if found == 0:
        print("\nRecord not found!")
    fp_grades.close()

def grade_statistics():
    total = 0
    min_grade = 100
    max_grade = 0
    a_grade = 0
    b_grade = 0
    c_grade = 0
    d_grade = 0
    f_grade = 0
    count = 0
    
    fp_grades = open("data/grades.csv", "r")
    for line in fp_grades:
        record = line.rstrip()
        fields = record.split(",")
        grade = int(fields[2])
        if(min_grade > grade):
            min_grade = grade
        if(max_grade < grade):
            max_grade = grade
        total += grade
        count += 1
        
        if(grade >= 80 and grade <= 100):
            a_grade += 1
        elif(grade >= 70 and grade <= 79):
            b_grade += 1
        elif(grade >= 60 and grade <= 69):
            c_grade += 1
        elif(grade >= 50 and grade <= 59):
            d_grade += 1
        elif(grade >= 0 and grade <= 49):
            f_grade += 1
        
    avg = round(total/count,2)
        
    print("Class average: "+str(avg)+"%")
    print("Maximum grade: "+str(max_grade)+"%")
    print("Minimum grade: "+str(min_grade)+"%")
    print("A grade students: "+str(a_grade))
    print("B grade students: "+str(b_grade))
    print("C grade students: "+str(c_grade))
    print("D grade students: "+str(d_grade))
    print("F grade students: "+str(f_grade))
    
    fp_grades.close()

def get_name():
    first = input("Enter first name of the student: ")
    last = input("Enter last name of the student: ")
    first = get_proper_case_name(first).rstrip()
    last = get_proper_case_name(last).rstrip()
    return first, last

#grade validation and returning the value
def get_grade():
    grade = 0
    while True:
        try:
            grade = int(round(float(input("Enter grade of the student: ")),0))
            if grade < 0 or grade > 100:
                raise Exception
        except:
            print("Invalid value for grade! Try again.")
        else:
            break;
    return grade
        
if __name__ == '__main__':
    
    selection = get_menu_selection()
    
    while selection != 'E':
        if selection == 'D':
            first, last = get_name()
            delete_record(first, last)
        elif selection == 'I':
            first, last = get_name()
            grade = get_grade()
            insert_record(first, last, grade)
            copy_scratch()
        elif selection == 'F':
            first, last = get_name()
            find_record(first, last)
        elif selection == 'S':
            grade_statistics()
            
        selection = get_menu_selection()
        
    print("\nThank you for using YourName's grade application!")        
            
            
            
            
            
            
            
            
            
            
            
            
            
            