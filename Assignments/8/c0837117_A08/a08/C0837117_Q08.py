# Assignment 08
# c0837117 - Asif Mahmud
# Question 08
# Date of submission: 2021-11-29

#function to get the first letter capitalized
def get_proper_case_name(name):
    correct_case_name = ""
    for ch in range(0, len(name)):
        if ch == 0:
            correct_case_name = name[ch].upper()
        else:
            correct_case_name += name[ch].lower()
    
    return correct_case_name

#reading file
def read_file(file):
    names = []
    for line in file:
        name = line.rstrip()
        names.append(name)
    return names    

#validating whether the user has given proper consent
def validate_user_consent(gender):
    isYes = ""
    if gender == "m":
        isYes = input("Do you want to enter a boy's name (Y/N): ")
    else:
        isYes = input("Do you want to enter a girl's name (Y/N): ")
        
    while(isYes not in ("y", "Y", "n", "N")):
        print("\nInvalid choice! Please try again.")
        if gender == "m":
            isYes = input("Do you want to enter a boy's name (Y/N): ")
        else:
            isYes = input("Do you want to enter a girl's name (Y/N): ")
    return isYes

#getting input from the user      
def get_input(gender):
    nameInput = ""
    isYes = validate_user_consent(gender)
    if(isYes == "y" or isYes == "Y"):
        if gender == "m":
            nameInput = get_proper_case_name(input("Enter the boy's name: "))
        else:
            nameInput = get_proper_case_name(input("Enter the girl's name: ")) 
    return nameInput

#checking the user input against the list
def check_if_popular(nameList, name):
    f = 0
    for fileName in nameList:
        if fileName == name:
            print(name+" is one of the popular names.")
            f = 1
            break
    if f == 0 :
        print(name+" is not one of the popular names.")
              
if __name__ == '__main__':
    fp_boys = open("data/BoyNames.txt")
    fp_girls = open("data/GirlNames.txt")
    
    boyNames = read_file(fp_boys)
    girlNames = read_file(fp_girls)
        
    fp_boys.close()
    fp_girls.close()
      
    boyInput = get_input("m")
    girlInput = get_input("f")
    
    if boyInput:
        check_if_popular(boyNames, boyInput)
    if girlInput:
        check_if_popular(girlNames, girlInput)
            
    