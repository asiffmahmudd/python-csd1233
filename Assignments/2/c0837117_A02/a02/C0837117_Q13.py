# Assignment 02
# c0837117 - Asif Mahmud
# Question 13
# Date of submission: 2021-09-25

if __name__ == '__main__':
    V = E = R = S = 0
    R = float(input("Enter the length of the row, in feet:"))
    E = float(input("Enter the amount of space used by an end-post assembly, in feet:"))
    S = float(input("Enter the space between vines, in feet:"))
    V = R-(2*E*S)
    print("Number of vines that will fit in the row: "+str(V))