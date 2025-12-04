import random

for child in range(10):
    score = random.randint(1,101)
    if score > 50:
        print("Child =", child, "Score =", score, "Good")
    else:
        print("Child =", child, "Score =", score, "Naughty")