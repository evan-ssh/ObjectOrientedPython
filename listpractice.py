#Extract unique characters from multiple strings
#fruits = ["apple", "banana", "grape", "orange"]
#uniqueChars = []
#for fruit in fruits:
#    for char in fruit:
#        if char not in uniqueChars:
#            uniqueChars.append(char)
#print(uniqueChars)

#Flatten list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8], [9]]
flatten_list = []
for i in nested_list:
    flatten_list.extend(i)
print(flatten_list)
#Find all divisors of a number (n)