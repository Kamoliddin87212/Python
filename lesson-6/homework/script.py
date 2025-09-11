#1. Modify String with Underscores
def insert_underscore(txt):
    result = ""
    i = 0
    while i < len(txt):
        result += txt[i]
        if (i + 1) % 3 == 0 and i < len(txt) - 1:
            if txt[i] in "aeiou" or (i+1 < len(txt) and txt[i+1] == '_'):
                result += txt[i+1] + "_"
                i += 1
            else:
                result += "_"
        i += 1
    return result

print(insert_underscore("abcabcabcdeabcdefabcdefg"))

#2. Integer Squares Exercise
n = int(input("Enter a number: "))
for i in range(n):
    print(i**2)

# Loop-Based Exercises

## Exercise 1: Print first 10 natural numbers using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1

## Exercise 2: Print the following pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

## Exercise 3: Calculate sum of all numbers from 1 to a given number
n = int(input("Enter number "))
print("Sum is:", sum(range(1, n + 1)))

## Exercise 4: Print multiplication table of a given number
n = int(input())
for i in range(1, 11):
    print(n * i)

## Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)

## Exercise 6: Count the total number of digits in a number
num = int(input())
count = 0
while num != 0:
    num //= 10
    count += 1
print(count)

## Exercise 7: Print reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

## Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)-1, -1, -1):
    print(list1[i])

## Exercise 9: Display numbers from -10 to -1 using a for loop
for i in range(-10, 0):
    print(i)

## Exercise 10: Display message “Done” after successful loop execution
for i in range(5):
    print(i)
else:
    print("Done!")

## Exercise 11: Print all prime numbers within a range
start = 25
end = 50
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

## Exercise 12: Display Fibonacci series up to 10 terms
a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b

## Exercise 13: Find the factorial of a given number
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! = {fact}")

# Return Uncommon Elements of Lists

## Exercise 1: Return the elements that are not common between two lists.
from collections import Counter
def uncommon(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []
    for k, v in c1.items():
        if k not in c2:
            result.extend([k] * v)
    for k, v in c2.items():
        if k not in c1:
            result.extend([k] * v)
    return result

