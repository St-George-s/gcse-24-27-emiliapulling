# Question 11
# code = "rzy"
# userInput = input("Enter code: ")
# while code != userInput:
#     print("NO")
#     userInput = input("Please re-enter code: ")
# print("Code accepted")

# Question 12
# code = "4003"
# userInput = input("Enter code: ")
# while code != userInput:
#     print("NO")
#     userInput = input("Please re-enter code: ")
# print("Code accepted")

# Question 13
# userInput = int(input("Enter age: "))
# while userInput <= 14:
#     print("NO")
#     userInput = int(input("Please re-enter age: "))
# print("Age accepted")

# Question 14
# password = input("Enter password: ")
# while len(password) < 5:
#     password = input("Password not long enough, please re-enter: ")
# print("Password accepted")

# Question 15
# anotherEpisode = input("would you like to watch more modern family?")
# while anotherEpisode == "yes":
#     print("playing another episode")
#     anotherEpisode = input("would you like to watch more modern family?")
# print("See you later!")

# Question 16
money = (int(input("enter amount of money: ")))
while money < 100:
    money = money + int(input("more money please: "))
print("I accept your offer")
print("You gave me", money)