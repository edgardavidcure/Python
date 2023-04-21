
from ast import While
import numbers
import random

#Magic Number example
magic_number = int(input ("What is the magic number? "))
user_guess = int(input ("What is your guess? "))

while magic_number != user_guess:
    if magic_number > user_guess:
        print("Higher")
        user_guess = int(input ("What is your guess? "))
    elif magic_number < user_guess:
        print("Lower")
        user_guess = int(input ("What is your guess? "))


if magic_number == user_guess:
    print("You guessed it!")
else: 
    print("That is not a number... ")



#Random Number

number = random.randint(1,100)
user_guess = int(input ("What is your guess? "))
count = 1

while number != user_guess:
    if number > user_guess:
        print("Higher")
        user_guess = int(input ("What is your guess? "))
        count +=1
    elif number < user_guess:
        print("Lower")
        user_guess = int(input ("What is your guess? "))
        count +=1


if number == user_guess:
    print("You guessed it!")
else: 
    print("That is not a number... ")

print (f"It took you {count} guesses. ")

#Play again loop
play_again = input ("Would you like to play again? Yes/No: ").lower()
while play_again == "yes":
    number = random.randint(1,100)
    user_guess = int(input ("What is your guess? "))
    count = 1
    while number != user_guess:
        if number > user_guess:
            print("Higher")
            user_guess = int(input ("What is your guess? "))
            count +=1
        elif number < user_guess:
            print("Lower")
            user_guess = int(input ("What is your guess? "))
            count +=1

        if number == user_guess:
            print("You guessed it!")
        
    print (f"It took you {count} guesses. ")
    play_again = input ("Would you like to play again? Yes/No: ").lower()