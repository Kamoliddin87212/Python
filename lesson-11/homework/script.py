## Exercise 1: Create your own virtual environment and install some python packages.
# This is command line:
# python -m venv myenv
# myenv\Scripts\activate
# pip install requests numpy

## Exercise 2: Create custom modules.
# math_operations.py
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b if b != 0 else "Error"

# string_utils.py
def reverse_string(s):
    return s[::-1]
def count_vowels(s):
    return sum(1 for c in s if c.lower() in 'aeiou')

## Exercise 3: Create custom packages.
# geometry/__init__.py empty

# geometry/circle.py
import math
def calculate_area(radius):
    return math.pi * radius ** 2
def calculate_circumference(radius):
    return 2 * math.pi * radius

# file_operations/__init__.py empty

# file_operations/file_reader.py
def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

# file_operations/file_writer.py
def write_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)
