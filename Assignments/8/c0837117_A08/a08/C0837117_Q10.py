# Assignment 08
# c0837117 - Asif Mahmud
# Question 10
# Date of submission: 2021-11-29

#reading file
def read_file(file):
    champions = []
    for line in file:
        record = line.rstrip()
        champions.append(record)
    return champions 

#getting input from the user
def get_input():
    return input("Enter the name of the team: ")

#making each word's first letter capitalized
def get_proper_case_name(name):
    correct_case_name = ""
    for ch in range(0, len(name)):
        if ch == 0 or (ch > 0 and name[ch-1] == " "):
            correct_case_name += name[ch].upper()
        else:
            correct_case_name += name[ch].lower()
    
    return correct_case_name

if __name__ == '__main__':
    fp_champions = open("data/WorldSeriesWinners.txt")
    champions = read_file(fp_champions)
    
    user_team = get_proper_case_name(get_input())
    count = 0
    for team in champions:
        if team == user_team:
            count += 1
            
    print(user_team+" has won the world series "+str(count)+" times")