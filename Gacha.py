def DeliveryDate():                             #function allowing user to choose desired delivery date
    print("Enter desired delivery date:")
    month = 13
    day = 32
    while (month>12):
        month = int(input("Enter month(MM): "))
    if (month == 1):
        while (day>31):
            day = int(input("Enter day(DD): "))
    elif (month == 2):
        while (day>28):
            day = int(input("Enter day(DD): "))
    elif (month == 3):
        while (day>31):
            day = int(input("Enter day(DD): "))
    elif (month == 4):
        while (day>30):
            day = int(input("Enter day(DD): "))
    elif (month == 5):
        while (day>31):
            day = int(input("Enter day(DD): "))
    elif (month == 6):
        while (day>30):
            day = int(input("Enter day(DD): "))
    elif (month == 7):
        while (day>31):
            day = int(input("Enter day(DD): "))
    elif (month == 8):
        while (day>31):
            day = int(input("Enter day(DD): "))
    elif (month == 9):
        while (day>30):
            day = int(input("Enter day(DD): "))
    elif (month == 10):
        while (day>31):
            day = int(input("Enter day(DD): "))
    elif (month == 11):
        while (day>30):
            day = int(input("Enter day(DD): "))
    elif (month == 12):
        while (day>31):
            day = int(input("Enter day(DD): "))
    if month > 2:                               #jump to next year if past february 
        year = 2021
    else:
        year = 2022
    date = month , day , year
    print("Your selected delivery date is: ", date)
    return date

def CalcCost(customer_list):                    #function to calculate total of order
    total = 0

    for i in customer_list:                     #loop through list and sum up numbers
        total += i
    
    return total
