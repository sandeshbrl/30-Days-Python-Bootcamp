
#1. Number Sign Checker

num = float(input('Enter any number:'))
if num>0:
    print('The number is positive')
elif num<0:
    print('The number is negative')
else:
    print('The number is zero')
    
#2. Driving Eligibility
    
age = int(input('Enter your age:'))

if age>=18:
    print('You are eligible for driving license')
    
else:
    print('You are ineligible for driving license')

    
#3. Grading System
    
marks = float(input('Enter your marks: '))
if marks>=90:
    print('Your Grade is:', 'A')
elif marks<90 and marks>=75:
    print('Your Grade is:', 'B')
elif marks<75 and marks>=60:
    print('Your Grade is:', 'C')
else:
    print('Your Grade is:', 'F')
    
    
#4. Nested Login Check
    
is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("Welcome Admin")
    else:
        print("Welcome User")
else:
    print("Please log in")
    
#5. Max of three numbers
    
num1 = float(input('Enter number one:'))
num2 = float(input('Enter number two:'))
num3 = float(input('Enter number three:'))

if num1>num2 and num1>num3:
    print('The Max number is:', num1)
elif num2>num3:
    print('The Max number is:', num2)
else:
    print('The Max number is:', num3)


#6. Even or Odd Checker
    
num = float(input('Enter any number: '))

if num%2 == 0:
    print('Even Number')
else:
    print('Odd Number')

#7. Password Validator
    
predefined_pass = "admin123"
password = input('Enter your password:')

if password == predefined_pass:
    print('Access Granted')
else:
    print('Access Denied')
    
#8. Check Leap Year
    
current_year = int(input('Enter the current year:'))
if (current_year % 4 == 0):
    print(f'{current_year} is a Leap Year')
else:
    print(f'{current_year} is not a Leap year')
    
    
#9. Temperature Converter
    
tempr = float(input('Enter the current temperature:'))
unit = input('Is the temperature is in Celsius (C) or Fahrenheit (F)?').strip().upper()

if unit == "C":
    fahrenheit = (tempr * 9/5) + 32
    print (f'{tempr}°C is {fahrenheit}°F')
elif unit == "F":
    celsius = (tempr - 32) * 5/9
    print (f'{tempr}°F is {celsius}°C')
    
    
#10. Rock Paper Scissors Game
    
import random

user_choice = input("Choose rock, paper, or scissors: ").lower()
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

print(f"You chose {user_choice}. Computer chose {computer_choice}.")

if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win")
    else:
        print("You lose")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win")
    else:
        print("You lose")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win")
    else:
        print("You lose")

    
