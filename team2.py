grade = float(input("What is the grade percentage? "))
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else: letter = "F"

# stretch challenge 1
if grade % 10 < 3:
    sign = "-"
elif grade % 10 >= 7:
    sign = "+"
else: sign = ""
#stretch challenge 2
if grade >= 93:
    sign = ""
#stretch challenge 3
if grade < 60:
    sign = ""

print (f"Your grade is: {letter}{sign}")

if grade >= 70:
    print("Congratulations! You passed the class!")
else: print ("I am sorry, you did not passed the class. You can do better next time!")















