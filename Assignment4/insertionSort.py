import csv
import time
import random
filename = "testData.csv"
def openFile(filename):
    testInfo = []
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            totaltime = row[0]
            range = row[1]
            testInfo.append((totaltime,range))
    return testInfo

def writeFile(numberRange,totalTime):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow([numberRange,totalTime])
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j-1] 
            j -=  1

def main():
    arr = []
    numberRange = 2000
    for _ in range(numberRange):
        arr.append(random.randint(1,100))
    startTime = time.time()
    insertionSort(arr)
    endTime = time.time()
    totalTime = endTime - startTime
    print(totalTime)
    writeFile(numberRange, totalTime)
if __name__ == "__main__":
    main()