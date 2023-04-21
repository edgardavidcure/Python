

variable = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."


play_again = "yes"
while play_again == "yes":
    favourite_number = int(input ("Enter your favourite number: "))
    for k, letter in enumerate(variable):
            if k % favourite_number == 0:
                print (letter.upper(), end="")
            else:
                print (letter.lower(), end="")
    print()
    play_again = input("Would you like to play again? Yes/No: ").lower()
print()
print("See ya! ")

            

