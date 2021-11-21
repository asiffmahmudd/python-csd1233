# Assignment 07
# c0837117 - Asif Mahmud
# Question 02
# Date of submission: 2021-11-21

#writing year in output file
def write_year(prev_year, fp_output):
    if(prev_year == "1"):
        fp_output.write("\n\t\tFreshman: "+str(year_total))
    elif(prev_year == "2"):
        fp_output.write("\n\t\tSophomore: "+str(year_total))
    elif(prev_year == "3"):
        fp_output.write("\n\t\tJunior: "+str(year_total))

if __name__ == '__main__':
    
    #opening files
    fp_enrollment = open("data/enrollment.csv", "r")
    fp_output = open("data/output.txt", "w")

    #initializing all variables
    is_first = True
    prev_school = ""
    prev_program = ""
    prev_year = ""
    curr_school = ""
    curr_program = ""
    curr_year = ""
    college_total = 0
    year_total = 0
    program_total = 0
    school_total = 0
    
    fp_output.write("STUDENT COUNT BY DEPARTMENT\n")
    
    #processing files
    for line in fp_enrollment:
        record = line.rstrip()
        fields = record.split(",")
        curr_school = fields[3]
        curr_program = fields[4]
        curr_year = fields[5]
        
        if(is_first):
            prev_school = fields[3]
            prev_program = fields[4]
            prev_year = fields[5]
            fp_output.write(prev_school+"\n\t"+prev_program)
            year_total = 1
            is_first = False
        #processing years
        elif(curr_year != prev_year):
            write_year(prev_year, fp_output)
            program_total += year_total
            year_total = 0
            prev_year = curr_year
            # processing program
            if(curr_program != prev_program):
                fp_output.write("\n\t"+prev_program+" TOTAL: "+str(program_total))
                school_total += program_total
                program_total = 0
                if(curr_school == prev_school):
                    fp_output.write("\n\t"+curr_program)
                prev_program = curr_program
                #processing school
                if(curr_school != prev_school):
                    fp_output.write("\n"+prev_school+" TOTAL: "+str(school_total))
                    college_total += school_total
                    school_total = 0
                    fp_output.write("\n"+curr_school)
                    fp_output.write("\n\t"+curr_program)
                    prev_school = curr_school
        else:
            year_total += 1            
    
    write_year(prev_year, fp_output)
    program_total += year_total
    school_total += program_total
    college_total += school_total
    
    #writing final program, school and college total
    fp_output.write("\n\t"+prev_program+" TOTAL: "+str(program_total))
    fp_output.write("\n"+prev_school+" TOTAL: "+str(school_total))
    fp_output.write("\nCOLLEGE WIDE TOTAL\t\t"+str(college_total))
          
    #closing files  
    fp_enrollment.close()
    fp_output.close()