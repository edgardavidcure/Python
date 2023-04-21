



secret_word = "edgar"
count = 1

print ("Welcome to the word guessing game!\n")

word_guess = input ("What is your guess? ").lower()

while word_guess != "edgar":
    print ("Your guess is not correct.")
    word_guess = input ("What is your guess? ").lower()
    count +=1

print (f"Congratulations! You guessed it!\nIt took you {count} guesses.")





















