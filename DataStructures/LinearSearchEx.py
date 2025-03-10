#Write a function which performs linear search.  The function should accept 2 arguments, an array to search with and a value to search for.  The function should return True or False.  Test the function by creating a list with 1000 random values and choose a random value to search for.


array = [1,23,4,1,3,4,6]
def search(array,value):
    for i in range(len(array)):
        if i == value:
            return True
        
    return False

test = search(array,3)
print(test)