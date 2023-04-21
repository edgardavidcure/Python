


def firstif():
    while True:
        print ("\nYou are walking through a dark forest and find three items: a MATCH, a PHONE, and a FLASHLIGHT. \nWhich one do you want to pick up?\n")
        first = input ("Type 'Match', 'Phone' or 'Flashlight: ").lower()
        if first == "match" :
            print ("\nYou pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out.\nDo you want to RUN, or HIDE behind a tree?\n")
            first_first = input ("Type 'Run' or 'Hide': ").lower()
            if first_first == "run":
                print ("\nYou keep running in the dark and you don't see the grizzly bear anymore. Do you want to CRY or PRAY for help?\n")
                first_second = input ("Type 'Cry' or 'Pray': ").lower()
                if first_second == "cry":
                    print ("\nYou start crying and someone listens to you. You hear a man saying 'Is there anybody here in the forest?'. Do you want to RESPOND or CLIMB a tree to see the man?\n")
                    first_third = input ("Type 'Respond' or 'Climb': ").lower()
                    if first_third == "respond":
                        print ("\nYou responded and the man finds you and takes you home. You are now safe. How lucky!\n")
                        break
                    elif first_third == "climb":
                        print ("\nYou climb the tree and notice that the man is your dad's friend.\nHe see's you in the tree and takes you home. You are now safe.\n ")
                        break
                    else: print ("\nHmm... that is not an option.  Please start over again.\n ")
                    
                elif first_second == "pray":
                    print ("\nYou start praying and someone listens to you. You hear a man saying 'Is there anybody here in the forest?'. Do you want to RESPOND or CLIMB a tree to see the man?\n ")
                    first_third = input ("Type 'Respond' or 'Climb': ").lower()
                    if first_third == "respond":
                        print ("\nYou responded and the man finds you and takes you home. You are now safe. How lucky!\n")
                        break
                    elif first_third == "climb":
                        print ("\nYou climb the tree and notice that the man is your dad's friend.\nHe see's you in the tree and takes you home. You are now safe.\n ")
                        break
                    else: print ("\nHmm... that is not an option.  Please start over again.\n ") 
                    
                else: print ("\nHmm... that is not an option.  Please start over again.\n ")
            elif first_first == "hide":
                print ("\nYou hide behind a tree and the grizzly bear is gone. Do you want to WALK away or SCREAM?\n")
                first_second = input ("Type 'Walk' or 'Scream': ").lower()
                if first_second == "walk":
                    print ("\nYou start walking and notice there is a man screaming 'Is there anybody here in the forest?'. Do you want to RESPOND or CLIMB a tree to see the man?\n")
                    first_third = input ("Type 'Respond' or 'Climb': ").lower()
                    if first_third == "respond":
                        print ("\nYou responded and the man finds you and takes you home. You are now safe. How lucky!\n")
                        break
                    elif first_third == "climb":
                        print ("\nYou climb the tree and notice that the man is your dad's friend.\nHe see's you in the tree and takes you home. You are now safe.\n ")
                        break
                    else: print ("\nHmm... that is not an option.  Please start over again.\n ")
                    
                elif first_second == "scream":
                    print ("\nYou start screaming and someone listens to you. You hear a man saying 'Is there anybody here in the forest?'. Do you want to RESPOND or CLIMB a tree to see the man?\n ")
                    first_third = input ("Type 'Respond' or 'Climb': ").lower()
                    if first_third == "respond":
                        print ("\nYou responded and the man finds you and takes you home. You are now safe. How lucky!\n")
                        break
                    elif first_third == "climb":
                        print ("\nYou climb the tree and notice that the man is your dad's friend.\nHe see's you in the tree and takes you home. You are now safe.\n ")
                        break
                    else: print ("\nHmm... that is not an option.  Please start over again.\n ")
                    
                else: print ("\nHmm... that is not an option.  Please start over again.\n ")
                
            else: print ("\nHmm... that is not an option.  Please start over again.\n ")
        elif first == "flashlight":
            print ("\nYou turn on the flashlight and the forest around you is illuminated. You see a large grizzly bear, and then the match burns \nDo you want to RUN, or HIDE behind a tree?\n")
            first_first = input ("Type 'Run' or 'Hide': ").lower()
            if first_first == "run":
                print ("\nYou keep running in the dark and you don't see the grizzly bear anymore. Do you want to CRY or PRAY for help?\n")
                first_second = input ("Type 'Cry' or 'Pray': ").lower()
                if first_second == "cry":
                    print ("\nYou start crying and someone listens to you. You hear a man saying 'Is there anybody here in the forest?'. Do you want to RESPOND or CLIMB a tree to see the man?\n")
                    first_third = input ("Type 'Respond' or 'Climb': ").lower()
                    if first_third == "respond":
                        print ("\nYou responded and the man finds you and takes you home. You are now safe. How lucky!\n")
                        break
                    elif first_third == "climb":
                        print ("\nYou climb the tree and notice that the man is your dad's friend.\nHe see's you in the tree and takes you home. You are now safe.\n ")
                        break
                    else: print ("\nHmm... that is not an option.  Please start over again.\n ")
                    
                elif first_second == "pray":
                    print ("\nYou start praying and someone listens to you. You hear a man saying 'Is there anybody here in the forest?'. Do you want to RESPOND or CLIMB a tree to see the man?\n ")
                    first_third = input ("Type 'Respond' or 'Climb': ").lower()
                    if first_third == "respond":
                        print ("\nYou responded and the man finds you and takes you home. You are now safe. How lucky!\n")
                        break
                    elif first_third == "climb":
                        print ("\nYou climb the tree and notice that the man is your dad's friend.\nHe see's you in the tree and takes you home. You are now safe.\n ")
                        break
                    else: print ("\nHmm... that is not an option.  Please start over again.\n ")
                    
                else: print ("\nHmm... that is not an option.  Please start over again.\n ")
                
            elif first_first == "hide":
                print ("\nYou hide behind a tree and the grizzly bear is gone. Do you want to WALK away or SCREAM?\n")
                first_second = input ("Type 'Walk' or 'Scream': ").lower()
                if first_second == "walk":
                    print ("\nYou start walking and notice there is a man screaming 'Is there anybody here in the forest?'. Do you want to RESPOND or CLIMB a tree to see the man?\n")
                    first_third = input ("Type 'Respond' or 'Climb': ").lower()
                    if first_third == "respond":
                        print ("\nYou responded and the man finds you and takes you home. You are now safe. How lucky!\n")
                        break
                    elif first_third == "climb":
                        print ("\nYou climb the tree and notice that the man is your dad's friend.\nHe see's you in the tree and takes you home. You are now safe.\n ")
                        break
                    else: print ("\nHmm... that is not an option.  Please start over again.\n ")
                    
                elif first_second == "scream":
                    print ("\nYou start screaming and someone listens to you. You hear a man saying 'Is there anybody here in the forest?'. Do you want to RESPOND or CLIMB a tree to see the man?\n ")
                    first_third = input ("Type 'Respond' or 'Climb': ").lower()
                    if first_third == "respond":
                        print ("\nYou responded and the man finds you and takes you home. You are now safe. How lucky!\n")
                        break
                    elif first_third == "climb":
                        print ("\nYou climb the tree and notice that the man is your dad's friend.\nHe see's you in the tree and takes you home. You are now safe.\n ")
                        break
                    else: print ("\nHmm... that is not an option.  Please start over again.\n ")
                    
                else: print ("\nHmm... that is not an option.  Please start over again.\n ")
                
            else: print ("\nHmm... that is not an option.  Please start over again.\n ")
            
        elif first == "phone" :
            print ("\nYou turn on the phone but you do not have the password. Do you want to do an emergency CALL to the police or turn on the phone FLASHLIGHT?\n")  
            first_first = input ("Type 'Call' or 'Flashlight': ").lower()
            if first_first == "call":
                print ("\nYou call the police and they start asking a few questions but you hear some weird sound close to you. Do you ANSWER their questions or stay QUIET?\n ")
                first_second = input("Type 'Answer' or 'Quiet': ").lower()
                if first_second == "answer":
                    print ("\nThe police gets your information and say that they are o their way to find you. Do you want to WAIT or keep finding your way OUT of the forest?\n")
                    first_third = input ("Type 'Wait' or 'Out': ").lower()
                    if first_third == "wait":
                        print ("\nAfter a few minutes waiting, the police finds you and takes you home. You are now safe.\n")
                        break
                    elif first_third == "out":
                        print ("\nYou walk for a few minutes and see the policemen coming your way. They find you and take you home. You are now safe.\n")
                        break
                    else: print ("\nHmm... that is not an option.  Please start over again.\n ")

                elif first_second == "quiet":
                    print ("\nYou stay quiet and realize that there is big shadow close to you. Do you want to RUN or turn on your phone FLASHLIGHT?\n")
                    first_third = input ("Type 'Run' or 'Flashlight': ").lower()
                    if first_third == "run":
                        print ("\nYou start running and find your way out of the forest. You know the way home. You are now safe.\n")
                        break
                    elif first_third == "flashlight":
                        print ("\nYou turn on the flashlight and find out that your dad's friend is the big shadow. You call him by his name, he see's you and takes you home.\nYou are now safe.\n")
                        break
                    else: print ("\nHmm... that is not an option.  Please start over again.\n ")
            elif first_first == "flashlight":
                print ("\nYour turn on the flashlight and see a big shadow close to the trees. Do you want to get CLOSER or turn OFF your flashlight?\n")
                first_second = input ("Type 'Closer' or 'Off': ").lower()
                if first_second == "closer":
                    print ("\nYou get closer to the shadow and realize there is a person walking. Do you TALK to him or start RUNNING?\n")
                    first_third = input ("Type 'Talk' or 'Running': ").lower()
                    if first_third == "talk":
                        print ("\nYou talk to the person and realize is your dad's friend. He takes you home.\nYou are now safe.\n")
                        break
                    elif first_third == "running":
                        print ("\nYou start running and find your way out of the forest.\nYou are now safe\n")
                        break
                    else: print ("\nHmm... that is not an option.  Please start over again.\n ")
                elif first_second == "off":
                    print ("\nYour turn off your flashlight but you cannot see anything anymore. You accidentally drop the phone and cannot find any other Item.\nDo you start CRYING or PRAYING?\n")
                    first_third = input ("Type 'Crying' or 'Praying': ").lower()
                    if first_third == "crying":
                        print ("\nYou start crying and someone hears you. Is the police. Your parents reported you dissapeard and they were looking for you.\nYou are now safe.\n ")
                        break
                    elif first_third == "praying":
                        print ("\nYou start praying out loud and all of a sudden someone calls you by your name. It is your dad's friend who has been looking for you.\nHe takes you home and you are safe.\n")
                        break
                    else: print ("\nHmm... that is not an option.  Please start over again.\n ")
                else: print ("\nHmm... that is not an option.  Please start over again.\n ")
            else: print ("\nHmm... that is not an option.  Please start over again.\n ")
        else: print ("\nHmm... that is not an option.  Please start over again.\n ")
firstif()


        