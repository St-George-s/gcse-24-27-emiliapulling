totalHeight = 0
counter = 0

for i in range(3):
    height = int(input("Tell me the height: "))
    totalHeight = totalHeight + height 
    counter = counter + 1

print("Average is", totalHeight / counter)