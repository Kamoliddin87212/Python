# Exercise 1: Determines whether a given year is a leap year.
print('Answer to Exercise 1:', end='')
year = int(input('Enter the year: '))
if year%4==0:
    if year%100 == 0:
        if year%400 == 0:
            print('leap year')
        else:
            print('not leap year')
    else:
        print('leap year')
else:
    print(year, 'is not leap year')

# Exercise 2: Conditional Statements Exercise
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird;
# If n is even and in the inclusive range of 2 to 5, print Not Weird;
# If n is even and in the inclusive range of 6 to 20, print Weird;
# If n is even and greater than 20, print Not Weird.
print('\nAnswer to Exercise 2:', end='')
ex2_weird_check = int(input('Enter a number for weird check:'))
if ex2_weird_check % 2 == 1:
    print("Weird")
elif 2 <= ex2_weird_check <= 5:
    print("Not Weird")
elif 6 <= ex2_weird_check <= 20:
    print("Weird")
else:
    print("Not Weird")

# Exercise 3: Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
# Give two solutions.
# Solution 1 with if-else statement.
# Solution 2 without if-else statement.
print('\nAnswers to Exercise 3:')
a = int(input("Enter first integer number: "))
b = int(input("Enter second integer number: "))
print("Solution 1:")
if a == b:
    print("No even numbers found.")
elif a - b == 2 or b - a == 2:
    print("No even numbers found.")
elif a%2 != 0:
    print('You did not enter an even number for "a"')
elif b%2 != 0:
    print('You did not enter an even number for "b"')
elif a < b:
    print('Even numbers between ', a, 'and', b, 'are: ', *range(a+2,b, 2))
else:
    print('Even numbers between ', b, 'and', a, 'are: ', *range(b+2, a, 2))
print("Solution 2:")
print("Even numbers between", a, "and", b, "are: ", end=' ')
while a < b-2:
    a = a + 2
    print(a, end=' ')
while b < a-2:
    b = b + 2
    print(b, end=' ')
