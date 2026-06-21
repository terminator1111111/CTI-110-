# M_R
# Jun 21, 2026
# Python Variables and Mathematical Expressions
# Integers & Floats

#import math to use the constant math.pi
import math

#Get radius from user
radius = float(input("What is the radius of the circle? "))
print()

#Calculate diameter
diametr = 2 * radius

#Display diameter with one decimal point 
print(f"The diameter of the circle is {diametr:.1f}\n")

#Calculate Circumference
circumference = 2 * math.pi * radius

#Display circumference with 2 decimal places
print(f"The circumference of the circle is {circumference:.2f}\n")

#calculate the area
area = math.pi * radius**2

#Display area with 3 decimal places
print(f"The area of the circle is {area:.3f}")
