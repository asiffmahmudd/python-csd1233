

if __name__ == '__main__':
    
    # resp = input("Please enter a numeric value:") #"123.45.89"
    # num = resp
    # num = num.replace(".", "", 1)
    #
    # while not num.isnumeric():
    #     resp = input("Please enter a numeric value:")
    #     num = resp
    #     num = num.replace(".", "", 1)
    #
    # num = float(resp)
    # print(num)
    
    try: 
        fp = open("does_not_exist.txt", 'r')
    except Exception:
        print("Something went wrong!")
        
    try:
        num1 = float(input("Please input a number:"))
        num2 = float(input("Please input another number:"))
        div = float(input("Please input another number:"))
        intermediate_res = num1 ** num2
        final_res = intermediate_res / div
    except OverflowError as expObj:
        print("The result is too large to store in the allocated memory")
        print(expObj)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except ValueError:
       print("Please provide only valid numbers")
    except Exception:
        print("An exception was raised!")
    else:
        print("Congrats, no exceptions were raised!")
    finally:
        print("This runs everytime; regardless of exceptions or not")
    