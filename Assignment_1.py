#1 Create a Python file and write five different messages.

print ('Hello, World')
print ('Coding is Fun')
print ('Python Bootcamp')
print(' 3 + 5 =', 3+5)
print('Wrapping Up')

#2 Function that prints your name and age.

def print_name_and_age ( ):  
    name = 'Sandesh'
    age = 24
    print('The Name is:' , name)
    print('The Age is:' , age)
print_name_and_age ( )

#3 Use comments to explain each line in your code

def print_name_and_age ( ): 
    #This Functions prints your name and age

    name = 'Sandesh'
    age = 24
    #These two functions store your name and age in variables

    print('The Name is:' , name)
    print('The Age is:', age)
    #These two functions print your name and age

print_name_and_age ( )
#Calls the function to run and show the output


#5 Simple Calculator that prints the sum of two numbers

num1 = float(input('Enter the first number:'))
num2 = float(input('Enter the second number:'))
result = num1 + num2
print ('The sum is:' , result)