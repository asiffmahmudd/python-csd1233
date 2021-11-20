
if __name__ == '__main__':
    
     #Step 01: Open the file for WRITE
    fp = open("new.txt", 'a')
    is_first_line = True
    
    first_name = input("Please enter student's first name (0 to terminate):")
    last_name = input("Please enter student's last name (0 to terminate):")
    grade = float(input("Please enter student's grade:"))
    
    while first_name != "0":
        #Step 02: Processing
        record = first_name + "," + last_name + "," + str(grade)
        
        if fp.tell() != 0: #tell method allows us byte offset where the file pointer is
            record = "\n" + record
            
        fp.write(record) 
        
        #Is there another student?
        first_name = input("Please enter student's first name (0 to terminate):")
        last_name = input("Please enter student's last name (0 to terminate):")
        grade = float(input("Please enter student's grade:"))
    
    #Step 03: Close the file
    fp.close()
