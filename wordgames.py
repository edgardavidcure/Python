

def start():  
    while True: 
        print ("\nWelcome to StoryLand!")
        start = input ("To start, enter the letter 'S': ").lower()
        if start == "s":
                print ("First, Let's gather some information:\n")
                date = input ("Type a date and press enter: ")
                adjective = input ("Type an adjective and press enter: ")
                animal = input ("Type an animal name and press enter: ")
                verb = input ("Type a Verb and press enter: ")
                exclamation = input ("Type an exclamation and press enter: ").capitalize()
                verb2 = input ("Type another Verb and press enter: ")
                verb3 = input ("Type another Verb again and press enter: ")
                print (f"\nGreat!\n\nYou are about to read the most weird but funny story on earth:\n\nThe other day, I was really in trouble. It was {date}, \nand it all started when I saw a very {adjective} {animal} {verb} inside my bedroom. \n{exclamation}! I yelled. But all I could think to do was to {verb2} over and over. \nMiraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family.\n")
                break
        else: print ("You have to enter the right letter to start.\nOtherwise, you won't enjoy Storyland.\nLet's start over again...")
start()




