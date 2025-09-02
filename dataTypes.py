# Data Types
name = "Emilia"# This is a string
myAge = 13 # This is an integer
height = 169.5 # This is a decimal number (float,real)
hasAPet = True # This is a boolean (True/False)

# Casting (Change from one data type to another)
age = input("Enter age: ")
print(age)
print(age + "10") # Concatenate two strings together (join them)
ageAsAnInt = int(age)
print(ageAsAnInt + 10) # Add two integers together (maths addition)
print("Your age is " + str(ageAsAnInt))

# Data types - more examples
stillAnIntetger = -4
myNumber = "07359098772" # Always store as a string

# Arithmetic operators
add = 10 + 10
subtract = 10 - 10
multiply = 10 * 10 
division = 10 / 10 # Will output a float
integerDivision = 11 / 10 # Forces output to be an integer
print(add, subtract, multiply, division)
print(integerDivision)
modulo = 5 % 4 # Remainder of the division
print(modulo)
exponent = 2 ** 3 # To the power of
print(exponent)

# Activity 1 - take two inputs, multiply them together and output answer
number = input("Enter a number: ")
number2 = input("Enter another number: ")
multiply = int(number) * int(number2)
print(multiply)
# Activity 2 - Input user's age, output age times 7
age = input("Enter age: ")
# Activity 3 - Take radius as input, output volume of sphere (v = 4/3 x pi x r^3)