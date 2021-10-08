# Assignment 03
# c0837117 - Asif Mahmud
# Question 15
# Date of submission: 2021-09-30

if __name__ == '__main__':
    input_seconds = int(input("Enter seconds: "))
    seconds = input_seconds
    days = hours = minutes = 0
    
    if(seconds >= 86400):
        days = int(seconds / 86400)
        seconds = seconds % 86400
    if(seconds >= 3600):
        hours = int(seconds / 3600)
        seconds = seconds % 3600
    if(seconds >= 60):
        minutes = int(seconds / 60)
        seconds = seconds % 60
    
    output_str = ""
    if(input_seconds >= 86400):
        output_str += str(days)+" days, "
    if(input_seconds >= 3600):
        output_str += str(hours)+" hours, "
    if(input_seconds >= 60):
        output_str += str(minutes)+" minutes, "
    output_str += str(seconds) + " seconds."
    
    print(output_str)