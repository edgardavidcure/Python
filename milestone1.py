
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










