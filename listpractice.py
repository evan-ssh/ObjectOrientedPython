#Extract unique characters from multiple strings
#fruits = ["apple", "banana", "grape", "orange"]
#uniqueChars = []
#for fruit in fruits:
#    for char in fruit:
#        if char not in uniqueChars:
#            uniqueChars.append(char)
#print(uniqueChars)

#Flatten list
#nested_list = [[1, 2, 3], [4, 5], [6, 7, 8], [9]]
#flatten_list = []
#for i in nested_list:
#    flatten_list.extend(i)
#print(flatten_list)
#Find all divisors of a number (n)

#n = 5
#factors = []
#for i in range(1, n+1):
#    if n % i == 0:
#        factors.append(i)
#print(factors)

#Elements in common between two lists
#fruits = ["apple","bannana","kiwi"]
#fruits2 = ["grape","watermelon","kiwi"]
#intersectFruits = [fruit for fruit in fruits if fruit in fruits2]
#print(intersectFruits)

#Find the First Occurrence of a Specific Value and return the index

numbers = [1,2,3,4,5,6]
number = 3
for i, value in enumerate(numbers,number):
    if value == number:
        print(f"{number} is at index {i}")
print("Number not found")