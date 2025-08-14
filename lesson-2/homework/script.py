#Task 1. Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
age = 2025 - birth_year
print(f"Name: {name}, Age: {age}.")

#Task 2. Extract car names from the following text: txt = 'LMaasleitbtui'
txt_car1 = 'LMaasleitbtui'
print(txt_car1[::2])
print(txt_car1[1::2])

#Task 3. Extract car names from the following text: txt = 'MsaatmiazD'
txt_car2 = 'MsaatmiazD'
print(txt_car2[::2])
txt_car3 = 'MsaatmiazD'
print(txt_car3[::-2])

#Task 4. Extract the residence area from the following text: txt = "I'am John. I am from London"
txt3 = "I'am John. I am from London"
print(txt3[21:27:1])

#Task 5. Write a Python program that takes a user input string and prints it in reverse order.
user_input = input('Enter your text:')
print(user_input[::-1])

#Task 6. Write a Python program that counts the number of vowels in a given string.
text_t6 = input("Enter a word: ").lower()
vowels = "aeiou"
count = sum(1 for char in text_t6 if char in vowels)
print("Number of vowels:", count)

#Task 7. Write a Python program that takes a list of numbers as input and prints the maximum value.
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Maximum value:", max(numbers))

#Task 8. Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
palindrome_check = input('Enter your word:')
if palindrome_check == palindrome_check[::-1]:
    print("It's palindrome")
else:
    print("It's not palindrome")

#Task 9. Write a Python program that extracts and prints the domain from an email address provided by the user.
email = input("Enter your email: ")
domain = email.split("@")[1]
print("Domain:", domain)

#Task 10. Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string

password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12))
print("Generated password:", password)
