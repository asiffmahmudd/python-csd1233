# Assignment 06
# c0837117 - Asif Mahmud
# Question 21
# Date of submission: 2021-11-09

import random

def getComputerInput():
    c_input = random.randint(1, 3)
    if c_input == 1:
        c_input = "rock"
    elif c_input == 2:
        c_input = "paper"
    else:
        c_input = "scissors"
    return c_input

def getUserInput():
    u_input = input("Enter 'rock', 'paper' or 'scissors': ")
    while(u_input != "rock" and u_input != "paper" and u_input != "scissors"):
        print("Invalid input!")
        u_input = input("Enter 'rock', 'paper' or 'scissors': ")
    return u_input

def calculateResult(c_input, u_input):
    result = 0
    if(c_input == "rock"):
        if(u_input == "scissors"):
            result = 1
        elif(u_input == "paper"):
            result = 2
    elif(c_input == "paper"):
        if(u_input == "rock"):
            result = 1
        elif(u_input == "scissors"):
            result = 2
    if(c_input == "scissors"):
        if(u_input == "paper"):
            result = 1
        elif(u_input == "rock"):
            result = 2
    return result
    
if __name__ == '__main__':
    result = 0
    while(result == 0):
        c_input = getComputerInput()
        u_input = getUserInput()
        result = calculateResult(c_input, u_input)
        if(result == 0):
            print("Computer chose "+c_input+". Draw. Play again.")
    
    if(result == 1):
        print("Computer chose "+c_input+". Computer won!")
    else:
        print("Computer chose "+c_input+". You won!")