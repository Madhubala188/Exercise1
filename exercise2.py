#Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
import math
# Ask for the user's input for the radius
radius = float(input("Enter the radius of the circle: "))
# Calculate the area of the circle
area = math.pi * radius ** 2
# Print the area of the circle
print(f"The area of the circle with radius {radius} is {area:.2f}")
