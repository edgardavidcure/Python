


from cmath import exp, pi, sqrt
from re import A
from this import d
import math 

print ("Welcome to the velocity calculator. Please enter the following: ")

m = float(input("Mass (in kg): "))
r = float(input("Radius of a bowling ball: "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
#A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder: "))
A = math.pi * r ** 2
c = 1/2 * p * A * C

equation = math.sqrt(m*g/c) * (1 - math.exp((-math.sqrt(m*g*c)/m)*t))


print(f"The inner value of c is: {c:.3f} ")
print(f"The velocity after {t} seconds is: {equation:.3f} m/s")














