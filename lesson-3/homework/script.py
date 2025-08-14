#Task 1. Create a list containing five different fruits and print the third fruit.
fruits = ['Apple', 'Banana', 'Peach', 'Grape', 'Cherry']
print("3rd fruit:", fruits[2])

#Task 2. Create two lists of numbers and concatenate them into a single list.
list_1 = [1, 7, 3, 2]
list_2 = [9, 4, 6]
list_1_2 = list_1 + list_2
print(list_1_2)

#Task 3. Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
list_7_1 = [23, 56, 67, 45, 83, 98, 52]
first_el = list_7_1[0]
middle_pos = len(list_7_1) // 2
middle_el = list_7_1[middle_pos]
last_el = list_7_1[-1]
extracted_list = [first_el, middle_el, last_el]
print(extracted_list)

#Task 4. Create a list of your five favorite movies and convert it into a tuple.
movies = ["Inception", "Interstellar", "Matrix", "Arrival", "Terminator"]
movies_tuple = tuple(movies)
print(movies_tuple)

#Task 5. Given a list of cities, check if "Paris" is in the list and print the result.
cities = ["Tashkent", "Dushanbe", "Paris", "Tokyo"]
print("Paris" in cities)

#Task 6. Create a list of numbers and duplicate it without using loops.
numbers_t6 = [23, 52, 73]
duplicate = numbers_t6 * 2
print(duplicate)

#Task 7. Given a list of numbers, swap the first and last elements.
numbers_t7 = [3, 4, 7, 9]
numbers_t7[0], numbers_t7[-1] = numbers_t7[-1], numbers_t7[0]
print(numbers_t7)

#Task 8. Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
tup = tuple(range(1, 11))
print(tup[3:8])

#Task 9. Create a list of colors and count how many times "blue" appears in the list.
colors = ["blue", "red", "blue", "green", "blue", "blue"]
print(colors.count("blue"))

#Task 10. Given a tuple of animals, find the index of "lion".
animals = ("tiger", "lion", "elephant")
print(animals.index("lion"))

#Task 11. Create two tuples of numbers and merge them into a single tuple.
tup_num_1 = (13, 562, 43)
tup_num_2 = (84, 65, 63)
merged = tup_num_1 + tup_num_2
print(merged)

#Task 12. Given a list and a tuple, find and print their lengths.
my_list = [1, 2, 3, 4, 5, 6, 7]
my_tuple = (8, 9, 10, 11, 12)
print(len(my_list), len(my_tuple))

#Task 13. Create a tuple of five numbers and convert it into a list.
tup_t13 = (1, 2, 3, 4, 5, 7, 8, 9)
tup_list = list(tup_t13)
print(tup_list)

#Task 14. Given a tuple of numbers, find and print the maximum and minimum values.
tup = (9883, 777, 345, 59, 32)
print("Max:", max(tup))
print("Min:", min(tup))

#Task 15. Create a tuple of words and print it in reverse order.
words = ("apple", "banana", "peach")
print(words[::-1])
