
loan = float(input ("On a Scale from 1-10. How large is the loan? "))
if loan >= 5:
    credit_history = float(input("On a Scale from 1-10. How good is your credit history? "))
    income = float(input("On a Scale from 1-10. How high is your income? "))
    if credit_history >= 7 and income >= 7:
        decision = True
    elif credit_history >= 7 or income >= 7:
        down_payment = float(input ("On a Scale from 1-10. How large is your down payment? "))
        if down_payment >= 5:
            decision = True
        else: decision = False
    else: decision = False
elif loan < 5:
    credit_history = float(input("On a Scale from 1-10. How good is your credit history? "))
    if credit_history >= 4:
        income = float(input("On a Scale from 1-10. How high is your income? "))
        down_payment = float(input ("On a Scale from 1-10. How large is your down payment? "))
        if income >= 7 or down_payment >= 7:
            decision = True
        elif income >= 4 and down_payment >= 4:
            decision = True
        else: decision = False
    else: decision = False
else: print ("Sorry, you made a mistake. Please start over.")
    

if decision:
    print ("Your loan is approved")
if not decision:
    print ("Your loan was denied")
    