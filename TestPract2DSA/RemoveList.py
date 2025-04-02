import random
def createList():
    randomNums = []
    for _ in range(2000):
        randomNums.append(random.randint(1,100))
    return randomNums
    


def removeList(randomNums,num):
    count = 0
    while num in randomNums:
        randomNums.remove(num)
        count +=1
    return count

def main():
    randomNums = createList()
    num = int(input("Enter number to remove"))
    count = removeList(randomNums,num)
    print(f"{num} was removed from list {count} times")

if __name__ == "__main__":
    main()