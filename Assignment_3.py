#1 Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operation.")



#2 Comparision Practise

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


#3 Logical Test (AND / OR)

age = int(input("Enter your age: "))
country = input("Enter your country: ")

if age >= 18 and country == "india":
    print("You are eligible to vote in India.")
else:
    print("You are not eligible to vote in India.")


#4. Membership Game
    
    
favorite_colors = ["red", "blue", "green", "black", "purple"]
color = input("Enter a color: ")

if color.lower() in favorite_colors:
    print(color, "is one of the favorite colors!")
else:
    print(color, "is not in the favorite color list.")


#5. Bitwise Fun
    
x = 5
y = 3

print("x =", x, "->", bin(x))
print("y =", y, "->", bin(y))
print("x & y =", x & y, "->", bin(x & y))
print("x | y =", x | y, "->", bin(x | y))
print("x ^ y =", x ^ y, "->", bin(x ^ y))
print("~x =", ~x, "->", bin(~x))
print("x << 1 =", x << 1, "->", bin(x << 1))
print("x >> 1 =", x >> 1, "->", bin(x >> 1))


#6. Even or Odd Check

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")
    
    
    
#7. Swap Two Variables (No Third Variable)
    
a = int(input("Enter value for A: "))
b = int(input("Enter value for B: "))

a = a + b
b = a - b
a = a - b

print("A =", a)
print("B =", b)


#8. Voter Eligibility Checker

age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ")

if age >= 18 and citizen.lower() == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    
    
#9. Identity vs Equality Operators
    
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print("list1 == list2:", list1 == list2)  # True – values are equal
print("list1 is list2:", list1 is list2)  # False – different memory locations


#10. Assignment Operators Practice

x = 10
print("Initial value:", x)

x += 5
print("After += 5:", x)

x -= 3
print("After -= 3:", x)

x *= 2
print("After *= 2:", x)

x /= 4
print("After /= 4:", x)

x %= 3
print("After %= 3:", x)