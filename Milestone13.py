#35.74 + 0.6215 * temperature - 35.75 * speed ** 0.16 + 0.4275 * temperature * speed ** 0.16

import math

speed = 0
temp = 0

def get_windchill(speed, temp):
    windchill = (35.74 + (0.6215 * temp) - (35.75 * (speed ** 0.16)) + ((0.4275 * temp) * (speed ** 0.16)))
    return windchill


def convert_cel_to_far(temp):
    temp = celsius * 9/5 + 32
    return temp

temp = int(input("What is the temperature? "))
now_get_windchill = get_windchill(speed, temp)

far_or_cel = input("Fahrenheit or Celsius (F/C)? ").lower()
now_get_temp = get_windchill(speed,temp)

if far_or_cel == "c":
    celsius = int(temp)
    temp = convert_cel_to_far(temp)
else:
    temp = int(temp)

for i in range(5,61,5):
    speed = i
    print (f"At temperature {temp:.1f}F, and wind speed {speed}, the windchill is: {get_windchill(speed,temp):.2f}F")





