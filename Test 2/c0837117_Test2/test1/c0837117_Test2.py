'''
# Test 2
# c0837117 - Asif Mahmud
# Date of submission: 2021-12-15
'''
SEATS_ROW = 8
SEATS_COLUMN = 10
CURRENT_BOOKING_NUMBER = 1

def initializeSeats(theatreArray):
    for r in range(SEATS_ROW):
        row = []
        for c in range(SEATS_COLUMN):
            row.append(0) 
        theatreArray.append(row)

def reserveSeats(theatreArray, numberOfSeats, preference):
    global CURRENT_BOOKING_NUMBER
    global SEATS_COLUMN
    global SEATS_ROW
    isReservePossible = True
    count = 0
    row_index = 0
    col_index = 0
    
    if preference == 2:
        row = SEATS_ROW-1
        col = SEATS_COLUMN-1
        row_index = row
        col_index = col
        while row_index >= 0:
            count = 0
            col_index = SEATS_COLUMN-1
            while col_index >= 0:
                if theatreArray[row_index][col_index] > 0:
                    count = 0
                else:
                    count += 1
                if count == numberOfSeats:
                    break
                col_index -= 1 
            if count == numberOfSeats:
                break 
            else:
                row_index -= 1
    else:
        row = 0
        col = 0
        row_index = row
        col_index = col
        
        while row_index < SEATS_ROW:
            count = 0
            while col_index < SEATS_COLUMN:
                if theatreArray[row_index][col_index] > 0:
                    count = 0
                else:
                    count += 1
                if count == numberOfSeats:
                    break
                col_index += 1    
            if count == numberOfSeats:
                break
            else:
                row_index += 1
            
    if count < numberOfSeats:
        isReservePossible = False    
        
    if isReservePossible:
        temp = col_index
        if preference == 2:
            while col_index < temp+numberOfSeats:
                theatreArray[row_index][col_index] = CURRENT_BOOKING_NUMBER
                col_index += 1
        else:
            while col_index > temp-numberOfSeats:
                theatreArray[row_index][col_index] = CURRENT_BOOKING_NUMBER
                col_index -= 1
        CURRENT_BOOKING_NUMBER += 1
    
    if not isReservePossible:
        print("Sorry the reservation was not possible\n")    
    return theatreArray
  
def reserveSeatsWithSpecifics(theatreArray, numberOfSeats, row, columnStart):
    global CURRENT_BOOKING_NUMBER
    global SEATS_COLUMN
    isReservePossible = True
    count = 0
    col_index = columnStart-1
    row = SEATS_ROW-row
    
    while col_index < SEATS_COLUMN:
        if theatreArray[row][col_index] == 0:
            count += 1
        else:
            count = 0
        if count == numberOfSeats:
            break
        col_index += 1 
        
    if count < numberOfSeats:
        isReservePossible = False  
    
    if isReservePossible:
        temp = col_index
        while col_index > temp-numberOfSeats:
            theatreArray[row][col_index] = CURRENT_BOOKING_NUMBER
            col_index -= 1
        CURRENT_BOOKING_NUMBER += 1
        
    if not isReservePossible:
        print("Sorry the reservation was not possible\n")    
        
    return theatreArray
   
def cancelSeats(theatreArray, bookingNumber):
    global SEATS_ROW
    global SEATS_COLUMN
    count = 0
    for row in range(SEATS_ROW):
        for col in range(SEATS_COLUMN):
            if theatreArray[row][col] == bookingNumber:
                theatreArray[row][col] = 0
                count += 1
    
    if count == 0:
        print("No seats with specified booking number could be located.\n")
    else:
        print()
 
def removeEmptySeatsRow(theatreArray, row):
    global SEATS_COLUMN
    row = SEATS_ROW-row
    last_index = -1
    for col in range(SEATS_COLUMN):
        if theatreArray[row][col] == 0:
            for element in range(col+1, SEATS_COLUMN):
                if theatreArray[row][element] > 0:
                    theatreArray[row][col] = theatreArray[row][element]
                    theatreArray[row][element] = 0
                    col += 1
 
def search(theatreArray, bookingNumber):
    count = 0
    for row in range(SEATS_ROW):
        for col in range(SEATS_COLUMN):
            if theatreArray[row][col] == bookingNumber:
                count += 1
                print("Row: "+str(SEATS_ROW-row)+", Seat "+str(col+1))
    if count == 0:
        print("No seats with specified booking number could be located.\n")
    else:
        print()
        
def totalBooked(theatreArray):
    count = 0
    for row in range(SEATS_ROW):
        for col in range(SEATS_COLUMN):
            if theatreArray[row][col] > 0:
                count += 1
    print("The total number of seats reserved in the theatre is "+str(count))
    return count
                       
def displayMap(theatreArray):
    for r in range(SEATS_ROW):
        if r != 0:
            print("Row-"+str(SEATS_ROW-r), end='\t')
        if r == 0:
            for c in range(SEATS_COLUMN):
                print("\tSeat-"+str(c+1), end='')
            print("\nRow-"+str(SEATS_ROW-r), end='\t')
        for c in range(SEATS_COLUMN):
            print((theatreArray[r][c]), end='\t')
        print()
    print()
 
def printMenu():
    print("MENU")
    print("   1. Reserve seats") 
    print("   2. Reserve seats with specific starting row and column")
    print("   3. Cancel reservation")
    print("   4. Remove empty seats from specific row")
    print("   5. Search for reservation")
    print("   6. Total seats booked")
    print("   7. Display theatre map")
    print("   8. Exit application")
  
def getUserSelection():
    userSelection = 0
    while not isinstance(userSelection, int) or (userSelection < 1 or userSelection > 8):
        try:
            printMenu()
            userSelection = int(input("\nUser selection: "))
        except:
            print("\nInvalid menu selection!")
        else:
            if userSelection < 1 or userSelection > 8:
                print("\nInvalid menu selection!")
    
    return userSelection

def getNumberOfSeats():
    numberOfSeats = 0
    while not isinstance(numberOfSeats, int) or numberOfSeats <= 0:
        try:
            numberOfSeats = int(input("Enter number of adjacent seats you require: "))
        except:
            print("\nInvalid input! Please try again.")
        else:
            if numberOfSeats <= 0:
                print("\nInvalid input! Please try again.")
                
    return numberOfSeats

def getPreference():
    preference = 0
    while not isinstance(preference, int) or (preference != 1 and preference != 2):
        try:
            preference = int(input("Preference of seating (1 for back, 2 for front):"))
        except:
            print("\nInvalid input! Please try again.")
        else:
            if preference != 1 and preference != 2:
                print("\nInvalid input! Please try again.")
                
    return preference

def getRow(userSelection):
    row = 0
    inputString = ""
    if userSelection == 2:
        inputString = "Enter row number you wish to book seats: "
    elif userSelection == 4:
        inputString = "Which row would you like to remove empty seats from: "
    while not isinstance(row, int) or not (row >= 1 and row <= 8):
        try:
            row = int(input(inputString))
        except:
            print("\nInvalid input! Please try again.")
        else:
            if not(row >= 1 and row <= 8):
                print("\nInvalid input! Please try again.")
                
    return row

def getColumnStart():
    columnStart = 0
    while not isinstance(columnStart, int) or not(columnStart >= 1 and columnStart <= 10):
        try:
            columnStart = int(input("Enter column/seat number you want your seats to begin at: "))
        except:
            print("\nInvalid input! Please try again.")
        else:
            if not(columnStart >= 1 and columnStart <= 10):
                print("\nInvalid input! Please try again.")
                
    return columnStart

def getBookingNumber(userSelection):
    bookingNumber = ''
    inputString = ""
    if userSelection == 3:
        inputString = "Reservation number you would like to cancel: "
    elif userSelection == 5:
        inputString = "Reservation number are you searching for: "
        
    while not isinstance(bookingNumber, int):
        try:
            bookingNumber = int(input(inputString))
        except:
            print("\nInvalid input! Please try again.")
                
    return bookingNumber

if __name__ == '__main__':
    theatreArray = []
    initializeSeats(theatreArray)
    userSelection = 0
    while(userSelection != 8):
        userSelection = getUserSelection()
        print()
        if userSelection == 1:
            numberOfSeats = getNumberOfSeats()
            preference = getPreference()
            reserveSeats(theatreArray, numberOfSeats, preference)
        elif userSelection == 2:
            numberOfSeats = getNumberOfSeats()
            row = getRow(userSelection)
            columnStart = getColumnStart()
            reserveSeatsWithSpecifics(theatreArray, numberOfSeats, row, columnStart)
        elif userSelection == 3:
            bookingNumber = getBookingNumber(userSelection)
            cancelSeats(theatreArray, bookingNumber)
        elif userSelection == 4:
            row = getRow(userSelection)
            removeEmptySeatsRow(theatreArray, row)
        elif userSelection == 5:
            bookingNumber = getBookingNumber(userSelection)
            search(theatreArray, bookingNumber)
        elif userSelection == 6:
            totalBooked(theatreArray)
        elif userSelection == 7: 
            displayMap(theatreArray)
    
    print("\nThanks for using the application!")
    