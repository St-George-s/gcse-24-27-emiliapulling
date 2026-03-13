# Linear Search
# Create an array
names = ["Debbie", "Jessie", "Vigdis", "Emilia"]
searchValue = "Emilia"
found = False
index = 0

# Conditional loops that stops when
# 1. searchValue is found
# 2. the search is at the end of the array names
while not found and index < len(names):
    if searchValue == names[index]:
        found = True
    else:
        index += 1

# After the loop (unindent)
if found:
    print("Found")
else:
    print("Not found")