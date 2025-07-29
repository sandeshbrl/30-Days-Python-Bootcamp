#1 Create variables to store your name, age and whether you are student (bool)

name = "Sandesh"
age = 24
is_student = True

#2 Print out the type of each variable

print(type(name))        # Output: <class 'str'>
print(type(age))         # Output: <class 'int'>
print(type(is_student))  # Output: <class 'bool'>

#3 Convert a string number (e.g "45") to an integer and add 10

num_in_string = "45"
number = int(num_in_string)
result = number + 10
print(result)            # Output: 55

#4 Try converting a float to an integer and print the result

float_number = 22.5
integer = int(float_number)
print(integer)     # Output: 22

#5 Use type() to check the type of a variable after conversion

print(type(number))   # Output: <class 'int'>
print(type(integer))      # Output: <class 'int'>
