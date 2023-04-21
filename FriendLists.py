friends = []
name = ""

while name != "End":
    name = input ("Type the name of a friend: ").capitalize()
    if name != "End":
        friends.append(name)
        
print ("Your friends are: ")

for friend in friends:
    print (friend)

