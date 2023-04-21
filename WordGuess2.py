






def split(word):
    return [char for char in word]



secret_word = split("laurin")

count = 0

letter_count = len(secret_word) 
hint = split(letter_count * "_")


res = ' '.join([str(item) for item in hint]) 


print (f"\nWelcome to the word guessing game!\nYou have 5 tries to guess the secret {letter_count} letter word!\n")
word_guess = ""




while word_guess != secret_word:
    if count < 5:
        res = ' '.join([str(item) for item in hint]) 

        print (f"Your hint is {res}")
            
        word_guess = split(input("What is your guess? ").lower())
        hint = split(letter_count * "_")
        for i in range(0,letter_count):
            secret_letter = secret_word[i]
            guess_letter = word_guess[i]
                
            if secret_letter == guess_letter:
                hint[i] = guess_letter.upper()  
            else:
                for j in range(0, letter_count):
                    if guess_letter == secret_word[j]:
                        hint[i] = guess_letter.lower()
                    else: 
                        for k in range (0,letter_count):
                            if guess_letter == secret_letter:
                                hint[i] = guess_letter.upper()
        count +=1
        if word_guess == secret_word:
            print (f"Congratulations! You guessed it! it took you {count} attempts!")
            break
    else:
        print ("You failed.\nTry again next time.")
        break
        
      
    



        

