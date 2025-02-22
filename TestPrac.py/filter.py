

#highest_num = 0
#for num in numbers:
#    if num > highest_num:
#        highest_num = num
#print(f"Highest number in list is {highest_num}")

#lowest_num = numbers[0]
#for num in numbers:
#    if lowest_num > num:
#       lowest_num = num
#print(f"Lowest number in list is {lowest_num}")
#strvalue = ''
#for num in numbers:
#   strvalue += str(num) + ','
#print(strvalue)

#numbercomma = ', '.join(map(str,numbers))
#print(numbercomma)




def returnNum(numbers,amount):
   for _ in range(amount):
    if numbers:
        usernumbers = numbers.pop(0)
        userNums.append(usernumbers)
def amountList():
    return len(numbers)
def ListNumbers():
    print("List of numbers:")
    for i in numbers:
        print(i)
def userNumbers():
    print(f"User numbers:")
    for i in userNums:
     print(i)
numbers = [12313,1,2,3,4,5434254,23424,123131,13,31231312,322131,31314542345,5235,354364,6]
userNums = []
while True:
    amountlist = amountList()
    print(f"Numbers left in list {amountlist}")
    if amountlist == 0:
        print("Dequeing Done")
        break
    amount = int(input("enter amount of numbers"))
    returnNum(numbers,amount)
    ListNumbers()
    userNumbers()





