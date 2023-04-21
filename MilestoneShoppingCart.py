#DATA LISTS
departments = ["groceries", "appliances", "furniture"]
groceries = ["bread", "egg", "milk", "apple", "banana"]
groceries_prices = [3.90, 0.80, 4.99, 2.19, 1.49]
appliances = ["microwave", "fridge", "oven", "blender", "tv"]
appliances_prices = [199.99, 1399.99, 799.99, 89.99, 1099.99]
furniture = ["couch", "desk", "chair", "bed", "carpet"]
furniture_prices = [1899.99, 499.99, 129.99, 899.99, 139.99]

#DEPARTMENTS LISTS
groceries_department = departments[0]
appliances_department = departments[1]
furniture_department = departments[2]

#GROCERIES LISTS
bread = groceries [0]
egg = groceries [1]
milk = groceries [2]
apple = groceries [3]
banana = groceries [4]

bread_price = groceries_prices[0]
egg_price = groceries_prices[1]
milk_price = groceries_prices[2]
apple_price = groceries_prices[3]
banana_price = groceries_prices[4]

#APPLIANCES LISTS
microwave = appliances[0]
fridge = appliances [1]
oven = appliances [2]
blender = appliances [3]
tv = appliances [4]

microwave_price = appliances_prices[0]
fridge_price = appliances_prices[1]
oven_price = appliances_prices[2]
blender_price = appliances_prices[3]
tv_price = appliances_prices[4]

#FURNITURE LISTS
couch = furniture[0]
desk = furniture[1]
chair = furniture[2]
bed = furniture[3]
carpet = furniture[4]

couch_price = furniture_prices[0]
desk_price = furniture_prices[1]
chair_price = furniture_prices[2]
bed_price = furniture_prices[3]
carpet_price = furniture_prices[4]

#ACTIONS LISTS
list_of_actions = ["view items", "add items", "view cart", "remove items", "compute total", "quit", "change department"]

view_items = list_of_actions[0]
add_items = list_of_actions[1]
view_cart = list_of_actions[2]
remove_items = list_of_actions[3]
compute_total = list_of_actions[4]
quit = list_of_actions[5]
change_department = list_of_actions[6]

cart = []
cart_prices = []

print()
print ("Welcome to BestBy!\n")
print (f"Our store has different departments where you can find what you need.\nHere they are: ")
print()
act = True
while act != quit:
    #SELECT DEPARTMENT
    for number, department in enumerate(departments, start=1):
        print (f"{number}. {department.capitalize()}")
    print()
    select_department = input ("Please select one to start shopping in that department: ").lower()

    #GROCERIES

    if select_department == groceries_department:
        print()
        print (f"Welcome to our {groceries_department} department\n")
        act = None
        while act != quit:
            print ("Here is a list of actions you can take:\n")
            for number, action in enumerate(list_of_actions, start = 1):
                print (f"{number}. {action.capitalize()}")
                
            
            print()
            act = input ("What would you like to do? ").lower()

            print()
            #VIEW OR ADD ITEMS
            if act == view_items or act == add_items:
                add_any = "yes"
                while add_any == "yes":
                    print()
                    print (f"Here is a list of the items available in our {groceries_department} department: ")
                    print()
                    for number, (article, price) in enumerate(zip(groceries, groceries_prices), start=1 ):
                            print (f"{number}. {article.capitalize()} - ${price:.2f}")
                    print()
                    add_to_cart = input ("What item would you like to add? ").lower()
                    if add_to_cart == bread:
                        cart.append(add_to_cart)
                        cart_prices.append(bread_price)
                        print (f"{add_to_cart.capitalize()} has been added to the cart.")
                    elif add_to_cart == egg:
                        cart_prices.append(egg_price)
                        cart.append(add_to_cart)
                        print (f"{add_to_cart.capitalize()} has been added to the cart.")
                    elif add_to_cart == milk:
                        cart.append(add_to_cart)
                        cart_prices.append(milk_price)
                        print (f"{add_to_cart.capitalize()} has been added to the cart.")
                    elif add_to_cart == apple:
                        cart.append(add_to_cart)
                        cart_prices.append(apple_price)
                        print (f"{add_to_cart.capitalize()} has been added to the cart.")
                    elif add_to_cart == banana:
                        cart.append(add_to_cart)
                        cart_prices.append(banana_price)
                        print (f"{add_to_cart.capitalize()} has been added to the cart.")
                    else:
                        not_in_list = input ("That item is not on the list. Would you like to add it? ").lower()
                        if not_in_list == "yes":
                            cart.append(add_to_cart)
                            not_in_list_price = float(input ("What is the price of the item? "))
                            cart_prices.append(not_in_list_price)
                            print (f"{add_to_cart.capitalize()} has been added to the cart.")
                            break
                    

                    print()
                    add_any = input("Would you like to add any other item? ").lower()
                    
            #VIEW CART
            elif act == view_cart:
                print (f"The items on your cart are:")
                print()
                for number, (cart_items, price) in enumerate(zip(cart, cart_prices), start=1):
                    print(f"{number}. {cart_items.capitalize()} - ${price:.2f}")
            #REMOVE ITEMS
            elif act == remove_items:
                print (f"The items on your cart are: ")
                for number, (cart_items, price) in enumerate(zip(cart, cart_prices), start=1):
                    print(f"{number}. {cart_items.capitalize()} - ${price:.2f}")
                remove = int(input("What items would you like to remove? Please enter the number of the item: "))
                if remove > number:
                    print("Sorry, that item number is not in the cart.")
                else:
                    remove = remove - 1
                    print (f"{cart[remove].capitalize()} has been removed")
                    del cart[remove] 
                    del cart_prices[remove]
                    
            elif act == compute_total:
                print (f"The items on your cart are: ")
                for number, (cart_items, price) in enumerate(zip(cart, cart_prices), start=1):
                    print(f"{number}. {cart_items} - ${price:.2f}")

                total = sum(cart_prices)
                print(f"The total is: ${total:.2f}")
            #QUIT
            elif act == quit:
                print ("Thank you for shopping at BestBy, see you next time!")
                print()
                break
            #CHANGE DEPARTMENT
            elif act == change_department:
                break
                
                
            
            print()
        
        else:
            print ("finally") 


    #APPLIANCES
            
    elif select_department == appliances_department:
        print()
        print (f"Welcome to our {appliances_department} department\n")
        act = None
        while act != quit:
            print ("Here is a list of actions you can take:\n")
            for number, action in enumerate(list_of_actions, start = 1):
                print (f"{number}. {action.capitalize()}")
                
            
            print()
            act = input ("What would you like to do? ").lower()

            print()
            if act == view_items or act == add_items:
                add_any = "yes"
                while add_any == "yes":
                    print()
                    print (f"Here is a list of the items available in our {appliances_department} department: ")
                    print()
                    for number, (article, price) in enumerate(zip(appliances, appliances_prices), start=1 ):
                            print (f"{number}. {article.capitalize()} - ${price:.2f}")
                    print()
                    add_to_cart = input ("What item would you like to add? ").lower()
                    if add_to_cart == microwave:
                        cart.append(add_to_cart)
                        cart_prices.append(microwave_price)
                        print (f"{add_to_cart.capitalize()} has been added to the cart.")
                    elif add_to_cart == fridge:
                        cart_prices.append(fridge_price)
                        cart.append(add_to_cart)
                        print (f"{add_to_cart.capitalize()} has been added to the cart.")
                    elif add_to_cart == oven:
                        cart.append(add_to_cart)
                        cart_prices.append(oven_price)
                        print (f"{add_to_cart.capitalize()} has been added to the cart.")
                    elif add_to_cart == blender:
                        cart.append(add_to_cart)
                        cart_prices.append(blender_price)
                        print (f"{add_to_cart.capitalize()} has been added to the cart.")
                    elif add_to_cart == tv:
                        cart.append(add_to_cart)
                        cart_prices.append(tv_price)
                        print (f"{add_to_cart.capitalize()} has been added to the cart.")
                    else:
                        not_in_list = input ("That item is not on the list. Would you like to add it? ").lower()
                        if not_in_list == "yes":
                            cart.append(add_to_cart)
                            not_in_list_price = float(input ("What is the price of the item? "))
                            cart_prices.append(not_in_list_price)
                            print (f"{add_to_cart.capitalize()} has been added to the cart.")
                            break
                    

                    print()
                    add_any = input("Would you like to add any other item? ").lower()

            elif act == view_cart:
                print (f"The items on your cart are:")
                print()
                for number, (cart_items, price) in enumerate(zip(cart, cart_prices), start=1):
                    print(f"{number}. {cart_items.capitalize()} - ${price:.2f}")
            elif act == remove_items:
                print (f"The items on your cart are: ")
                for number, (cart_items, price) in enumerate(zip(cart, cart_prices), start=1):
                    print(f"{number}. {cart_items.capitalize()} - ${price:.2f}")
                remove = int(input("What items would you like to remove? Please enter the number of the item: "))
                if remove > number:
                    print("Sorry, that item number is not in the cart.")
                else:
                    remove = remove - 1
                    print (f"{cart[remove].capitalize()} has been removed")
                    del cart[remove] 
                    del cart_prices[remove]
            elif act == compute_total:
                print (f"The items on your cart are: ")
                for number, (cart_items, price) in enumerate(zip(cart, cart_prices), start=1):
                    print(f"{number}. {cart_items} - ${price:.2f}")

                total = sum(cart_prices)
                print(f"The total is: ${total:.2f}")
            elif act == quit:
                print ("Thank you for shopping at BestBy, see you next time!")
                print()
                break
            elif act == change_department:
                break
            
            print()
        
        else:
            print ("finally")          

    #FURNITURE

    elif select_department == furniture_department:
        print()
        print (f"Welcome to our {furniture_department} department\n")
        act = None
        while act != quit:
            print ("Here is a list of actions you can take:\n")
            for number, action in enumerate(list_of_actions, start = 1):
                print (f"{number}. {action.capitalize()}")
                
            
            print()
            act = input ("What would you like to do? ").lower()

            print()
            if act == view_items or act == add_items:
                add_any = "yes"
                while add_any == "yes":
                    print()
                    print (f"Here is a list of the items available in our {furniture_department} department: ")
                    print()
                    for number, (article, price) in enumerate(zip(furniture, furniture_prices), start=1 ):
                            print (f"{number}. {article.capitalize()} - ${price:.2f}")
                    print()
                    add_to_cart = input ("What item would you like to add? ").lower()
                    if add_to_cart == couch:
                        cart.append(add_to_cart)
                        cart_prices.append(couch_price)
                        print (f"{add_to_cart.capitalize()} has been added to the cart.")
                    elif add_to_cart == desk:
                        cart_prices.append(desk_price)
                        cart.append(add_to_cart)
                        print (f"{add_to_cart.capitalize()} has been added to the cart.")
                    elif add_to_cart == chair:
                        cart.append(add_to_cart)
                        cart_prices.append(chair_price)
                        print (f"{add_to_cart.capitalize()} has been added to the cart.")
                    elif add_to_cart == bed:
                        cart.append(add_to_cart)
                        cart_prices.append(bed_price)
                        print (f"{add_to_cart.capitalize()} has been added to the cart.")
                    elif add_to_cart == carpet:
                        cart.append(add_to_cart)
                        cart_prices.append(carpet_price)
                        print (f"{add_to_cart.capitalize()} has been added to the cart.")
                    else:
                        not_in_list = input ("That item is not on the list. Would you like to add it? ").lower()
                        if not_in_list == "yes":
                            cart.append(add_to_cart)
                            not_in_list_price = float(input ("What is the price of the item? "))
                            cart_prices.append(not_in_list_price)
                            print (f"{add_to_cart.capitalize()} has been added to the cart.")
                            break
                    

                    print()
                    add_any = input("Would you like to add any other item? ").lower()

            elif act == view_cart:
                print (f"The items on your cart are:")
                print()
                for number, (cart_items, price) in enumerate(zip(cart, cart_prices), start=1):
                    print(f"{number}. {cart_items.capitalize()} - ${price:.2f}")
            elif act == remove_items:
                print (f"The items on your cart are: ")
                for number, (cart_items, price) in enumerate(zip(cart, cart_prices), start=1):
                    print(f"{number}. {cart_items.capitalize()} - ${price:.2f}")
                remove = int(input("What items would you like to remove? Please enter the number of the item: "))
                if remove > number:
                    print("Sorry, that item number is not in the cart.")
                else:
                    remove = remove - 1
                    print (f"{cart[remove].capitalize()} has been removed")
                    del cart[remove] 
                    del cart_prices[remove]
            elif act == compute_total:
                print (f"The items on your cart are: ")
                for number, (cart_items, price) in enumerate(zip(cart, cart_prices), start=1):
                    print(f"{number}. {cart_items} - ${price:.2f}")

                total = sum(cart_prices)
                print(f"The total is: ${total:.2f}")
            elif act == quit:
                print ("Thank you for shopping at BestBy, see you next time!")
                print()
                break
            elif act == change_department:
                break
            
            print()
        
    else:
        print()
        print("That does not seem right... Try again. ")
        print()

