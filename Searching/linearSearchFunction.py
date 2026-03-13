def linearSearch(searchValue, searchList):
    found = False
    index = 0

    while not found and index < len(searchList):
        if searchValue == searchList[index]:
            found = True
        else:
            index += 1

    if found:
        print("Found at", index)
    else:
        print("Not found")

linearSearch("Bob", ["Debbie", "Jessie", "Vigdis", "Emilia"])
linearSearch("Emilia", ["Debbie", "Jessie", "Vigdis", "Emilia"])
linearSearch(10, [4, 3, 34, 10])
