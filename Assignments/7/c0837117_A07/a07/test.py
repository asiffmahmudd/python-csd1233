def insert_line(fp_scratch, adding_line):
    if fp_scratch.tell() != 0:
        adding_line = "\n"+adding_line
    elif fp_scratch.tell() == 0:
        adding_line += "\n"
    fp_scratch.write(adding_line)
    print("Record inserted successfully")
    
def insert_record(first, last, grade):
    adding_line = first + "," + last + "," + str(grade)
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
            if first < fields[0]:
                insert_line(fp_scratch, adding_line)
                inserted = 1
            elif first == fields[0]:
                if last < fields[1]:
                    insert_line(fp_scratch, adding_line)
                    inserted = 1
                elif last == fields[1] and grade <= int(fields[2]):
                    insert_line(fp_scratch, adding_line)
                    inserted = 1
        fp_scratch.write(record)
    if inserted == 0:
        fp_scratch.write("\n"+adding_line)
        print("Record inserted successfully")
    
    
def copy_scratch():
    
    fp_scratch = open("data/scratch.csv", "r")
    fp_grades = open("data/grades.csv", "w")
    
    for record in fp_scratch:
        fp_grades.write(record)
        
    fp_scratch.close()
    fp_grades.close()
    
if __name__ == '__main__':
    first = input("Enter first name of the student: ")
    last = input("Enter last name of the student: ")
    grade = int(round(float(input("Enter grade of the student: ")),0))
    insert_record(first, last, grade)