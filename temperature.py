temperature = int(input ("What is the temperature in fahrenheit? "))
celsius = (temperature - 32) * 5/9
print (f"The temperature in celsius is: {celsius:.1f}")
if celsius >= 100:
    print ("It is boiling!")
elif celsius <= 0:
    print ("It is freezing!")