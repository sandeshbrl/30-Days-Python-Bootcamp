#1 Create a function greet_teacher(name) that greets the teacher by name

def greet_teacher(name):
    print(f"Hello, Teacher {name}! Welcome to the class.")

greet_teacher("Anita")


#2 Write a function multiply(a, b) that returns the product of two numbers

def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(f"Product of 4 and 5 is {result}")


#3 Write a function to calculate the total price after tax

def total_price_after_tax(price, tax_rate):
    tax_amount = price * (tax_rate / 100)
    total = price + tax_amount
    return total

total = total_price_after_tax(1000, 13)  # 13% tax
print(f"Total price after 13% tax on 1000 is {total}")


#4 Define a function to print employee details: name, position, salary

def print_employee_details(name, position, salary):
    print(f"Employee Name: {name}")
    print(f"Position: {position}")
    print(f"Salary: ${salary:.2f}")

print_employee_details("Ankit", "Manager", 50000)


#5 Write a function to convert Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_f = celsius_to_fahrenheit(25)
print(f"25°C is equal to {temp_f}°F")


#6 Create a function that returns the square of a number

def square(number):
    return number ** 2

print(f"Square of 7 is {square(7)}")


#7 Write a function that calculates simple interest

def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

si = simple_interest(10000, 5, 3)  # Principal=10,000, Rate=5%, Time=3 years
print(f"Simple interest is {si}")


#8 Create a function to print a birthday message with name and age

def birthday_message(name, age):
    print(f"Happy Birthday, {name}! You are now {age} years old.")

birthday_message("Samir", 25)


#9 Write a function to split a bill among friends

def split_bill(total_bill, number_of_friends):
    if number_of_friends == 0:
        return "Cannot split bill among zero friends!"
    amount_per_person = total_bill / number_of_friends
    return amount_per_person

split_amount = split_bill(1200, 4)
print(f"Each friend should pay: {split_amount}")


#10 Create a function that converts hours into minutes and seconds

def hours_to_minutes_seconds(hours):
    minutes = hours * 60
    seconds = hours * 3600
    return minutes, seconds

mins, secs = hours_to_minutes_seconds(2)
print(f"2 hours = {mins} minutes and {secs} seconds")

