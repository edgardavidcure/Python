




quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."


play_again = "yes"
while play_again == "yes":
    user_number = int(input ("What is your favourite number? ").lower())
    for i, letter in enumerate(quote):
        if i % user_number == 0:
            print (f"{letter.upper()}", end="")
        else:
            print(letter.lower(), end="")
    print()
    play_again = input ("Would you like to play again? ")
else:
    print("See ya! ")





















