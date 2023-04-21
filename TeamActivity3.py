
variable = "commitment"

favourite_letter = input ("Enter your favourite letter: ").lower()



for letter in variable:
    if letter.lower() == favourite_letter:
        letter = "_"  #or letter.upper() 
        print (f"{letter}", end="")
    else:
        print(letter.lower(), end="")


    
