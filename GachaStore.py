fout = open('GSReceipt.txt', 'w')
from random import randrange
import Gacha

class Technology:
    def __init__(self, name):
        self.name = name

class StuffedToy:
    def __init__(self, name):
        self.name = name

    def display(self):
        print (self.name)

class Device(Technology):
    def __init__(self, x, rank, prob):
        super().__init__(x)
        self.rank = rank
        self.prob = prob

    def display(self):
        print(self.name, "Rank: ", self.rank, "Probability: ", self.prob, "%")
    
class Component(Technology):
    def __init__(self, x, rank, prob):
        super().__init__(x)
        self.rank = rank
        self.prob = prob

    def display(self):
        print(self.name, "Rank: ", self.rank, "Probability: ", self.prob, "%")

#List of items in Technology Banner
device1 = Device('iBuyPower Gaming PC', '5 Star', 1)
device2 = Device('Samsung Note 20 Ultra', '5 Star', 1)
device3 = Device('iPad Pro', '5 Star', 1)
device4 = Device('Samsung SmartWatch', '4 Star', 20)
device5 = Device('Nintendo Switch', '4 Star', 20)
device6 = Device('Apple Watch SE', '4 Star', 20)
device7 = Device('Apple Airpods', '4 Star', 20)
device8 = Device('Amazon Echo Dot', '3 Star', 79)
device9 = Device('Logitech G502', '3 Star', 79)
device10 = Device('Logitech G213', '3 Star', 79)

comp1 = Component('GTX 3080 Ti', '5 star', 1)
comp2 = Component('Lian Li UNI', '3 Star', 79)

#List of items in Stuffed Toy Banner
toy1 = StuffedToy('Pikachu')
toy2 = StuffedToy('Kirby')
toy3 = StuffedToy('Klee')
toy4 = StuffedToy('Rilakkuma')
toy5 = StuffedToy('Hello Kitty')

greeting = "Welcome to the Gacha Store:"

banners = {"1": ("Tech Banner", 88.88), "2": ("Stuffed Toy Banner", 9.99)}

print(greeting)
print("Current available banners:")

for key, value in banners.items():
    print("{}) {}: ${} per pull" .format(key, value[0], value[1]))

#Allow user to choose to look at the items within each banner before selection
keep_beginning = 'N'
while keep_beginning != 'Y':            #while loop to allow going back and viewing the other banner info 
    print("\n")
    print("Enter 1 to view items in Tech Banner")
    print("Enter 2 to view items in Stuffed Toy Banner")
    print("Enter 3 to begin your order")
    begin = int(input())
    if (begin == 1):            #to see items and info of Technology Banner
        print("\n")
        print("TECHNOLOGY BANNER ITEMS:")
        comp1.display()
        device1.display()
        device2.display()
        device3.display()
        device4.display()
        device5.display()
        device6.display()
        device7.display()
        device8.display()
        device9.display()
        device10.display()
        comp2.display()
        print("\n")
        keep_beginning = input("Ready to begin your order? (Y for yes, N for No): ").upper()    #break out of while loop

    elif (begin == 2):          #to see items and info of Stuffed Toy Banner
        print("\n")
        print("STUFFED TOY BANNER ITEMS:")
        toy1.display()
        toy2.display()
        toy3.display()
        toy4.display()
        toy5.display()
        print("\n")
        keep_beginning = input("Ready to begin your order? (Y for yes, N for No): ").upper()    #break out of while loop

    elif (begin == 3):          #to immediately go to selection
        keep_beginning = 'Y'

    else:                       #if user does not enter 1,2, or 3
        print("\n")
        raise Exception("Invalid Input")
        keep_beginning = input("Ready to begin your order? (Y for yes, N for No): ").upper()

customer_list = []          #list that holds price of each item selected
temp_list = []              #temporary list that adds amount of particular banner into roll list
roll_list = []              #list with quantity of repeating numbers (1's and 2's) to allow for random pulling in correct banners

keep_choosing = "Y"
while keep_choosing == "Y":     #while loop to allow user to go back and forth during selection to add from both lists as many times as desired
    choice = str(input("\nEnter banner choice: "))      #user selects banner
    quant = int(input("Enter desired quantity: "))      #user selects quantity of pulls for the particular banner

    temp_list = choice * quant      #add selected banner quantity amount of times
    #print("temp list: " , temp_list) <- used for testing and debugging
    
    if choice in banners.keys():
        for i in range(quant):
            customer_list.append((banners[choice][1]))  #add selection price to customer list quantity amount of times
    else:
        print("That is an invalid choice. Skipping...") #skip invalid entries
        temp_list = []          #clear temp list for next iteration

    roll_list.extend(temp_list)     #extend roll list with temp list to have quantity of both banners in one list
    keep_choosing = input("Keep Choosing (Y for yes, N for no): ").upper()      #to break out of while loop

#print("cust list:", customer_list) <- used for testing and debugging
#print("roll list:", roll_list) <- used for testing and debugging

print("\n")

num1 = roll_list.count("1")         #count amount of pulls for technology banner
num2 = roll_list.count("2")         #count amoung of pulls for stuffed toy banner

rollbanner1 = []        #list for random ints for quantity of pulls for technology banner
rollbanner2 = []        #list for random ints for quantity of pulls for toy banner

order = []              #list to hold names of all items from pulling of both banners

date = Gacha.DeliveryDate()             #function call from custom module to request user's desired delivery date
total = Gacha.CalcCost(customer_list)   #function call from custom module to calculate total price

confirm = "N"
while confirm != "Y":       #while loop to stay until confirmation is approved
    print("\n")
    print("CHECKOUT:")
    print("Please confirm order total and delivery date:")
    print("${:.2f}" .format(total))         #output total price formatted to two decimal places
    print(date)
    confirm = input("Enter Y to confirm and checkout: ").upper()    #to break out of while loop

for i in range(num1):
    rollbanner1.append(randrange(400))      #pull technology banner, quantity amount of times

for i in range(num2):
    rollbanner2.append(randrange(5))        #pull stuffed toy banner, quantity amount of times

#print(rollbanner1) <- used for testing and debugging
#print(rollbanner2) <- used for testing and debugging

#use random integers from rollbanners1 list for technology banner to determine and add items to order list
for i in rollbanner1:           
    if i == 399:
        order.append(device1.name)
    if i == 398:
        order.append(device2.name)
    if i == 397:
        order.append(device3.name)
    if i == 396:
        order.append(comp1.name)
    if (i < 396 and i >= 376):
        order.append(device4.name)
    if (i < 376 and i >= 356):
        order.append(device7.name)
    if (i < 356 and i >= 336):
        order.append(device6.name)
    if (i < 336 and i >= 316):
        order.append(device7.name)
    if (i < 316 and i >= 237):
        order.append(device8.name)
    if (i < 237 and i >= 158):
        order.append(device9.name)
    if (i < 158 and i >= 79):
        order.append(device10.name)
    if (i < 79 and i >=0):
        order.append(comp2.name)

#use random integers from rollbanners2 list for stuffed toy banner to determine and add items to order list
for i in rollbanner2:
    if i == 0:
        order.append(toy1.name)
    if i == 1:
        order.append(toy2.name)
    if i == 2:
        order.append(toy3.name)
    if i == 3:
        order.append(toy4.name)
    if i == 4:
        order.append(toy5.name)

print("\n")
print("Congrats! You will recieve: ")
for i in order:             #output items that will be recieved 
    print("-", i)

#write out information to receipt
fout.write('*****RECEIPT*****\n')
fout.write('Total: ${:.2f}' .format(total))
fout.write('\nDelivery Date: {}' .format(date))
fout.write('\nPacking List:')
for i in order:
    fout.write('\n-{}'.format(i))
fout.write("\n")
fout.write("Thanks for shopping at the Gacha Store")
fout.close()

#output exit message
print("\n")
print("Receipt has been created to GSReceipt.txt") 
print("Thank you for shopping at the Gacha Store")  
