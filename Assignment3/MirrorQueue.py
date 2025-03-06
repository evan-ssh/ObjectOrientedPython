characters = ["a","b","c"]
rerversedList = []
for char in characters:
    rerversedList.append(char)
rerversedList.reverse()
for char in rerversedList:
    characters.extend(rerversedList)
    break
print(characters)