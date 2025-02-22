numbers = [12313,1,2,3,4,5434254,23424,123131,13,31231312,322131,31314542345,5235,354364,6]

highest_num = 0
for num in numbers:
    if num > highest_num:
        highest_num = num
print(f"Highest number in list is {highest_num}")

lowest_num = numbers[0]
for num in numbers:
    if lowest_num > num:
        lowest_num = num
print(f"Lowest number in list is {lowest_num}")
strvalue = ''
for num in numbers:
    strvalue += str(num) + ','
print(strvalue)

numbercomma = ', '.join(map(str,numbers))
print(numbercomma)