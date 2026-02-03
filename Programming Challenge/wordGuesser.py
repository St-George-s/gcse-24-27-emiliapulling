import random
lettersGuessed = []
words = ["apple", "banana", "kiwi", "pineapple", "mango", "coconut"]
randNum = random.randint(0,5)
selectedWord = words[randNum]

userLetter = ""
lettersGuessed.append(userLetter)

blankWord = ""
for x in range (len(selectedWord)):
    blankWord = blankWord + "_"

while selectedWord != blankWord:
    userLetter = input("Enter a letter: ")
    found = False
    for i in range(len(selectedWord)):
        if selectedWord[i] == userLetter:
            found = True
            blankWord = blankWord[:i] + userLetter + blankWord[i + 1:]
    print(blankWord)

print("WELL DONE YOU GUESSED THE WORD!!!")