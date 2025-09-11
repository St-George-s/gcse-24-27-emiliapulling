# for counter in range(10):
#     print("Hello World")

# # Question 1
# for counter in range(10):
#     print("Emilia")

# # Question 2
# name = input("Enter your name: ")
# for counter in range(1000):
#     print(name)

# # Question 3
# name = input("Enter your name: ")
# for counter in range(1000):
#     print("Hello", name)

# #Question 4
# for counter in range(1,13):
#     print(counter * 8)

# # Question 5
# for counter in range(1,1001):
#     print(counter * 8)

# # Question 6
# for counter in range(1,13):
#     print("7 x", counter, "=" , 7 * counter)

# # Question 7
# for counter in range(10):
#     age = input("Enter an age: ")
#     print(age)

# #Question 8
# for counter in range(10):
#     age = int(input("Enter an age: "))
#     print(age + 10)

# #Question 9
# total = 0
# for counter in range(10):
#     age = int(input("Enter an age: "))
#     print(age)
#     total = total + age
#     print(total)
    
# #Question 10
# for counter1 in range(1,13):
#     print("")
#     print(counter1, "times table")
#     for counter2 in range(1,13):
#         print(counter1 , "x", counter2 , "=" , counter1 * counter2)

# Extension Activity
timesTable = int(input("Which times table?: "))
howFar = int(input("How far?: "))

for counter in range(1,howFar + 1):
    print(counter * timesTable)