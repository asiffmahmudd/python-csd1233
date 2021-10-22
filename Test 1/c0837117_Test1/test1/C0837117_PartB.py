# Test 01
# c0837117 - Asif Mahmud
# Part B
# Date of submission: 2021-10-22

if __name__ == '__main__':
    print("**********BUYING THE CAR************")
    car_price = float(input("Please enter purchase price of the car: "))
    while car_price < 0:
        print("Please enter a valid value")
        car_price = float(input("Please enter purchase price of the car: "))
        
    tax = car_price*.13
    principle = car_price+tax
    
    print("Taxes to be added (13%): "+str(tax))
    print("Purchase price with taxes: "+str(principle))
    
    loan_rate = float(input("Please enter loan rate (%): "))
    while loan_rate <= 0:
        print("Please enter a valid value")
        loan_rate = float(input("Please enter loan rate (%): "))
    loan_rate = loan_rate/100
    
    loan_duration = int(input("Please enter duration of the loan (years): "))
    while loan_duration < 0:
        print("Please enter a valid value")
        loan_duration = int(input("Please enter duration of the loan (years): "))
    
    monthly_purchase_cost = round(((loan_rate/12)*principle)/(1-pow((1+(loan_rate/12)),loan_duration*(-12))),2)
    
    print("Monthly cost of purchase: "+str(monthly_purchase_cost))
    
    print("*********LEASING THE CAR************")
    
    monthly_lease_price = float(input("Monthly Lease Price: "))
    lease_tax = round(monthly_lease_price*0.13,2)
    monthly_lease_cost = monthly_lease_price+lease_tax
    
    print("Taxes to be added: "+str(lease_tax))
    print("Total Monthly lease cost: "+str(monthly_lease_cost))
    
    print("*********COMPARISON***************")
    
    lease_duration = int(input("Please enter the duration you plan on keeping the car (years): "))
    while loan_duration < 0:
        print("Please enter a valid value")
        lease_duration = int(input("Please enter the duration you plan on keeping the car (years): "))
    
    print ("{:<8} {:<10} {:<15} {:<10}".format('Year','Month','Lease Total','Purchase Total'))
    
    loop_count = lease_duration if (lease_duration > loan_duration) else loan_duration
    lease_expense = 0
    purchase_expense = 0
    for year in range(1,loop_count+1):
        for month in range(1,13):
            if(year <= lease_duration):
                lease_expense += monthly_lease_cost
            if(year <= loan_duration):
                purchase_expense += monthly_purchase_cost
            
            lease_expense = round(lease_expense,2)
            purchase_expense = round(purchase_expense, 2)
            
            if(year <= lease_duration):
                lease_ouput = str(lease_expense)
            else:
                lease_ouput = ""
            if(year <= loan_duration):
                purchase_output = str(purchase_expense)
            else:
                purchase_output = ""
            
            print("{:<8} {:<10} {:<15} {:<10}".format(year,month,lease_ouput,purchase_output))
    
    if(lease_expense < purchase_expense):
        print("Based on the information provided if you plan to keep your vehicle for "+str(lease_duration)+" years it is cheaper to lease")
    else:
        print("Based on the information provided if you plan to keep your vehicle for "+str(loan_duration)+" years it is cheaper to purchase")
    
    
    
    
    
    
    
    
    
    
    
    