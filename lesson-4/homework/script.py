#Task 1.1. Write a Python script to sort (ascending and descending) a dictionary by value.
dic_t11 = {'a': 3, 'b': 1, 'c': 2}
print("Ascending:", dict(sorted(dic_t11.items(), key=lambda x: x[1])))
print("Descending:", dict(sorted(dic_t11.items(), key=lambda x: x[1], reverse=True)))

#Task 1.2. Write a Python script to add a key to a dictionary. Sample Dictionary: {0: 10, 1: 20}. Expected Result: {0: 10, 1: 20, 2: 30}
dic_t12 = {0: 10, 1: 20}
dic_t12[2] = 30
print(dic_t12)

#Task 1.3. Write a Python script to concatenate the following dictionaries to create a new one.
#Sample Dictionaries:
#dic1 = {1: 10, 2: 20}
#dic2 = {3: 30, 4: 40}
#dic3 = {5: 50, 6: 60}
#Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {**dic1, **dic2, **dic3}
print(result)

#Task 1.4. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
#Sample Dictionary (n = 5):
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n = 5
dic_t14 = {x: x**2 for x in range(1, n+1)}
print(dic_t14)

#Task 1.5. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Expected Output:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
dic_t15 = {x: x**2 for x in range(1, 16)}
print(dic_t15)

#Task 2.1. Write a Python program to create a set.
set_t21 = {11, 25, 33}
print(set_t21)

#Task 2.2. Write a Python program to iterate over sets.
set_22 = {"apple", "banana", "cherry"}
for item in set_22:
    print(item)

#Task 2.3. Write a Python program to add member(s) to a set.
set_23 = {1, 2, 3}
set_23.add(4)
set_23.update([5, 6])
print(set_23)

#Task 2.4. Write a Python program to remove item(s) from a given set.
set_24 = {1, 2, 3, 4}
set_24.remove(3)
set_24.discard(4)
print(set_24)

#Task 2.5. Write a Python program to remove an item from a set if it is present in the set.
my_set = {1, 2, 3}
if 2 in my_set:
    my_set.remove(2)
print(my_set)
