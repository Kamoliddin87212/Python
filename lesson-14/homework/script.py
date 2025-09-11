## Exercise 1: JSON Parsing
import json
with open("students.json", "r") as f:
    students = json.load(f)
for student in students:
    print(student)

## Exercise 2: Weather API
import requests
city = "Tashkent"
api_key = "your_key"  # need key
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
data = requests.get(url).json()
print(data['main']['temp'], data['main']['humidity'])

## Exercise 3: JSON Modification
import json
# Assume books.json exists
with open("books.json", "r") as f:
    books = json.load(f)
# Add new
new_book = {"title": "New", "author": "Author"}
books.append(new_book)
# Update
for book in books:
    if book["title"] == "Old":
        book["author"] = "New Author"
# Delete
books = [b for b in books if b["title"] != "Delete"]
with open("books.json", "w") as f:
    json.dump(books, f)

## Exercise 4: Movie Recommendation System
import requests
import random
genre = input("Genre: ")
api_key = "your_key"
url = f"http://www.omdbapi.com/?s=movie&apikey={api_key}&type=movie"
data = requests.get(url).json()
movies = data['Search']
random_movie = random.choice(movies)
print(random_movie['Title'])


