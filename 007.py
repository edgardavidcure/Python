# Agent 007

def start():
    while True:
        print ("\nWelcome to Sanchez's restaurant\n\nWe encourage you to look at our menu. But...\n")
        ready = input ("Are you ready to order? 'Yes' or 'No': ").lower()
        if ready == "yes":
            print ("Perfect!, let's get your order")
            first_name = input ("What is your first name? ")
            last_name = input ("What is your last name? ")
            print (f"Awesome!, {last_name}, {first_name} {last_name}. Your food will be ready soon.\nYour Order number is 007\n")
            break
        elif ready == "no":
            print ("Well... at this point you don't have an option. Let's get your order")
            first_name = input ("What is your first name? ")
            last_name = input ("What is your last name? ")
            print (f"welcome! {last_name}, {first_name} {last_name}. Your food will be ready soon.\n Your Order number is 007\n")
            break
        else: print ("Hmm... You have to type 'Yes' or 'No'.\nLet's start over...")  
start()

def start1():  
    while True: 
        print ("\n\nWhile you wait for your food, let me read you a story!")
        start = input ("To start, enter the letter 'S': ").lower()
        if start == "s":
                print ("First, Let's gather some information:\n")
                date = input ("Type a date and press enter: ")
                adjective = input ("Type an adjective and press enter: ")
                animal = input ("Type an animal name and press enter: ")
                verb = input ("Type a Verb and press enter: ")
                exclamation = input ("Type an exclamation and press enter: ").capitalize()
                verb2 = input ("Type another Verb and press enter: ")
                verb3 = input ("Type another Verb again and press enter: ")
                print (f"\nGreat!\n\nYou are about to read the most weird but funny story on earth:\n\nThe other day, I was really in trouble. It was {date}, \nand it all started when I saw a very {adjective} {animal} {verb} inside my bedroom. \n{exclamation}! I yelled. But all I could think to do was to {verb2} over and over. \nMiraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family.\n")
                break
        else: print ("You have to enter the right letter to start.\nOtherwise, you won't enjoy Storyland.\nLet's start over again...")
start1()

print ("Okay... Your food is ready now")

child_meal = float(input ("\nWhat is the price of a child's meal? "))
adult_meal = float(input ("What is the price of an adult's meal? "))
children = int(input ("How many children are there? "))
adults = int(input ("How many adults are there? "))
sales_tax = float(input ("What is the sales tax rate? "))



subtotal = (child_meal * children) + (adult_meal * adults)
psubtotal = round(subtotal, 3)
print(f"\nSubtotal: ${psubtotal}" )
tax = subtotal * (sales_tax/100)
ptax= round (tax, 2)
print(f"Sales Tax: ${ptax} ")
tip = subtotal * (20/100)
ptip = round (tip, 2)
volunteer = input("\nWould you like to give a tip? Please type 'Yes' or 'No': ").lower()
if volunteer == "yes":
    print(f"The suggested tip is: ${ptip}")
    agree = input ("Is that okay? Please type 'Yes' or 'No': ").lower()
    if agree == "yes":
        total = subtotal + tax + tip
        ptotal = round (total, 2)
        print(f"\nTotal: ${ptotal}")
        payment_amount = float(input("\nWhat is the payment amount?: "))
        change = payment_amount - total
        pchange = round(change, 2)
        print (f"Change: ${pchange}\n")
    elif agree == "no":
        volunteer_tip = float(input("How much would you like to tip? "))
        total = subtotal + tax + volunteer_tip
        ptotal = round (total, 2)
        print(f"Total: ${ptotal}")
        payment_amount = float(input("\nWhat is the payment amount?: "))
        change = payment_amount - total
        pchange = round(change, 2)
        print (f"Change: ${pchange}\n")
else :
    total = subtotal + tax 
    ptotal = round (total, 2)
    print(f"Total: ${ptotal}")
    payment_amount = float(input("\nWhat is the payment amount?: "))
    change = payment_amount - total
    pchange = round(change, 2)
    print (f"Change: ${pchange}\n")


    