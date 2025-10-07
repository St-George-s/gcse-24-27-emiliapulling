# Create arrays
heights = [2.4, 3.8, 0.4, 1.9]
names = ["Bob", "Dave", "Simon", "John"]

print(names[1]) # Prints Dave
print(heights[1]) # Prints 3.8

# Loops over names array and print
for counter in range(len(names)):
    print(names[counter]) # Counter is 0 then 1 then 2
    print(heights[counter])

# Append (Add) to array
heights.append(2.2)
names.append("Jimmy")

print(heights)
print(names)