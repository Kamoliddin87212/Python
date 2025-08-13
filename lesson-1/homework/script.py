# Task 1. Given a side of square. Find its perimeter and area.
import math

square_side = int(input('Side of the square:'))
square_perimeter = square_side*4
square_area = square_side**2
print(square_perimeter)
print(square_area)

# Task 2. Given diameter of circle. Find its length.
circle_diameter = int(input('Diameter of the circle:'))
circle_lenght = 2 * math.pi * circle_diameter / 2
print(circle_lenght)

# Task 3. Given two numbers a and b. Find their mean.
a = int(input('Enter a:'))
b = int(input('Enter b:'))
mean_a_b = (a + b)/2
print(mean_a_b)

# Task 4. Given two numbers a and b. Find their sum, product and square of each number.
mean_a_b = a + b
product_a_b = a * b
square_a = a**2
square_b = b**2
print(mean_a_b)
print(product_a_b)
print(square_a)
print(square_b)
