password1 = input("Enter a password: ")
while len(password1) < 8:
    print("Password too short")
    password1 = input("Enter a password: ")

capitalCount = 0
lowerCaseCount = 0

    
while capitalCount == 0:
    for letter in password1:
        if ord (letter) >= 65 and ord (letter) <= 90:
            capitalCount = capitalCount + 1
    if capitalCount == 0:
        print("You need a capital letter, re-enter your password.")
        password1 = input("Enter a password: ")

while lowerCaseCount == 0:
    for letter in password1:
        if ord (letter) >= 97 and ord (letter) <= 122:
            lowerCaseCount = lowerCaseCount + 1
    if lowerCaseCount == 0:
        print("You need a lower case letter, re-enter your password.")
        password1 = input("Enter a password: ")

reenterPassword = input("Please enter your password again: ")
while reenterPassword != password1:
    print("That isn't the same password, try again.")
    reenterPassword = input("Please enter your password again: ")

if ord (letter) >= 33 and ord (letter) <= 64:
    print("Password is strong")
elif len(password1) >= 10:
    print("Password is medium strength")
else:
    print("Password is weak")

print("Password reset!")