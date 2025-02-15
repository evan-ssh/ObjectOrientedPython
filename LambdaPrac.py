#Lambda functions are functionnaly the same as a regular function in python
def add(x,y):
    return x+y
print(add(3,4))

#We dont need to add a return statement, lambda functions are known as anonymous functions
#addnum = lambda x,y: x+y
#print(addnum(3,4))

print((lambda x,y: x+y)(3,4))

#Lambdas are more useful when used with higher order functions

def my_map(my_func,my_iter): #How Map Works
    result = []
    for item in my_iter:
        new_item = my_func(item)
        result.append(new_item)
    return(result)
nums = [3,4,5,6,7,8]

cubed = my_map(lambda x: x**3, nums)#Lambda was passed to higher order function my map which was used to cube each number 
print(f"Cubed Numbers = {cubed}")