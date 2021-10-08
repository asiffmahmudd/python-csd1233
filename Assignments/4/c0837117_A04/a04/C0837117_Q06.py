# Assignment 04
# c0837117 - Asif Mahmud
# Question 06
# Date of submission: 2021-10-08


if __name__ == '__main__':
    celsius_temp = 0
    print("Celsius \t Fahrenheit")
    while(celsius_temp <= 20):
        fahrenheit_temp = (9/5)*celsius_temp + 32
        print(str(celsius_temp)+" \t\t "+ str("{:.2f}".format(fahrenheit_temp)))
        celsius_temp += 1