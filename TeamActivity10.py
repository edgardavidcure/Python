
bank_accounts = []
balances = []

name_account = None
while name_account != "quit":
    name_account = input ("What is the name of this account? ").lower()
    if name_account == "quit":
        break
    bank_accounts.append(name_account)
    current_balance = float(input("What is the balance? "))
    balances.append(current_balance)
   
if name_account == "quit":
    print()
    print ("Account information:")
    
    for i in range(len(bank_accounts)):
        bank_accounts[i]
        balances[i]
        print (f"{i}. {bank_accounts[i].capitalize()} - ${balances[i]:.2f} ")
    print()
    print (f"Total: ${sum(balances):.2f}")
    print (f"Average: ${sum(balances)/len(balances):.2f}")
    print (f"Highest balance: {bank_accounts[i]}: {max(balances):.2f}")
    print()

    





























