#1 Loop through a tuple of five favorite movies and print each one

favorite_movies = ("Inception", "Interstellar", "Lord of the Rings", "Parasite", "The Dark Knight")
for movie in favorite_movies:
    print(movie)

print("...................................")


#2 Use enumerate with a list of fruits, print index and fruit

fruits = ["apple", "banana", "grapes", "mango", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print("...................................")


#3 Use .items() on a dictionary of students and their grades

students_grades = {"Alice": 88, "Bob": 92, "Charlie": 79}
for student, grade in students_grades.items():
    print(f"{student}: {grade}")

print("...................................")


#4 Use .values() on a dictionary of countries and capitals, print only capitals

countries_capitals = {"Nepal": "Kathmandu", "India": "New Delhi", "Japan": "Tokyo"}
for capital in countries_capitals.values():
    print(capital)

print("...................................")

#5 Loop through a set of animal names and print each one

animal_names = {"dog", "cat", "elephant", "tiger", "lion"}
for animal in animal_names:
    print(animal)
    
print("...................................")

#6 Loop through dictionary keys only: products and prices, print product names only

products = {"pen": 10, "notebook": 40, "eraser": 5}
for product in products.keys():
    print(product)

print("...................................")


#7 Loop with range to generate first 10 even numbers and print them

for num in range(2, 21, 2): 
    print(num)

print("...................................")


#8 Loop through nested dictionary: students with age and grade, print name and grade

students = {
    "Alice": {"age": 20, "grade": 85},
    "Bob": {"age": 21, "grade": 90},
    "Charlie": {"age": 19, "grade": 78}
}
for student, details in students.items():
    print(f"{student}: Grade = {details['grade']}")

print("...................................")


#9 Loop through a user input string and print each character on a new line

user_input = input("Enter a string: ")
for char in user_input:
    print(char)

print("...................................")

#10 Use enumerate to build a menu and display numbered food items

food_items = ["Pizza", "Burger", "Momo", "Biryani", "Sandwich"]
print("Menu:")
for index, food in enumerate(food_items, start=1):
    print(f"{index}. {food}")

