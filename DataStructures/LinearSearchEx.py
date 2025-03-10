#Write a function which performs linear search.  The function should accept 2 arguments, an array to search with and a value to search for.  The function should return True or False.  Test the function by creating a list with 1000 random values and choose a random value to search for.
import random, time

array = []
for _ in range(1000000):
    array.append(random.randint(1,100))
    
searchValue = random.randint(1,100)

def search(array,searchValue):
    for i in array:
        if i == searchValue:
            return True
    return False

start_time = time.time()
test = search(array,searchValue)
print(test)
end_time = time.time()
total_time = end_time - start_time
print(total_time)