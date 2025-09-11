#1: Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

#2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    value = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input. Not an integer.")

#3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    with open("nofile.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")

#4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    a = input("Enter number 1: ")
    b = input("Enter number 2: ")
    if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit()):
        raise TypeError("Inputs must be numeric")
    print(float(a) + float(b))
except TypeError as e:
    print(e)

#5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
try:
    with open("file.txt", "r") as f:  # Assume permission issue
        pass
except PermissionError:
    print("Permission issue")

#6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
lst = [1,2,3]
try:
    print(lst[5])
except IndexError:
    print("Index out of range")

#7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    num = input("Enter number: ")
except KeyboardInterrupt:
    print("Input cancelled")

#8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    print(1 / 0)
except ArithmeticError:
    print("Arithmetic error")

#9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
try:
    with open("file.txt", encoding='ascii') as f:
        print(f.read())
except UnicodeDecodeError:
    print("Encoding issue")

#10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
lst = [1,2]
try:
    lst.appendd(3)
except AttributeError:
    print("Attribute does not exist")
