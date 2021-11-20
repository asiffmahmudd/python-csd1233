
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

#Copies the contents from sratch.csv file to grades.csv
def copy_scratch():
    
    fp_scratch = open("data/sratch.csv", "r")
    fp_grades = open("data/grades.csv", "w")
    
    for record in fp_scratch:
        fp_grades.write(record)
        
    fp_scratch.close()
    fp_grades.close()

#TODO: Add the functions for delete_record(), insert_record(), find_record(),
#get_statistics()
#In each of these functions you should OPEN, Process, and CLOSE the file grades.csv

def delete_record(first, last):
    pass #delete this when you add the logic

if __name__ == '__main__':
    
    selection = get_menu_selection()
    
    while selection != 'E':
        #TODO: LOGIC HERE
        
        selection = get_menu_selection()
        