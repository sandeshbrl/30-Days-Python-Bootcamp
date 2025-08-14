#1 Print numbers 1 to 10

i = 1
while i <= 10:
    print(i)
    i += 1

#2 Countdown number
    
n = int(input("Enter a number: "))
while n >= 0:
    print(n)
    n = n - 1


#3 Multiplication table
    
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#4 Skip multiples of 3
    
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

#5 First 5 even numbers
    
n = 1
count = 0

while True:
    if n % 2 == 0:
        print(n)
        count = count + 1
        if count == 5:
            break
    n = n + 1
    
    
#6 Reverse countdown timer
    
n = int(input("Enter a number: "))
while n >= 1:
    print(n)
    n = n - 1

#7 Break the loop on password match
    
correct_password = "python123"
while True:
    guess = input("Enter password: ")
    if guess == correct_password:
        print("Access granted")
        break

#8 Count vowels in a word
    
word = input("Enter a word: ")
count = 0
for letter in word:
    if letter.lower() in "aeiou":
        count = count + 1
print("Number of vowels:", count)

#9 Print all odd numbers from 1 to 50

for i in range(1, 51):
    if i % 2 == 0:
        continue
    print(i)

#10 Factorial calculator
    
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial is:", fact)

