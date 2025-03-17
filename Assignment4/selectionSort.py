import csv
import time
import random
def selectionSort(arr):
    for i in range(0, len(arr)-1):
        currentMinIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[currentMinIndex]:
                currentMinIndex = j
        arr[i],arr[currentMinIndex] = arr[currentMinIndex], arr[i]

def main():
    arr = []
    for _ in range(2000):
        arr.append(random.randint(1,100))
    startTime = time.time()
    selectionSort(arr)
    endTime = time.time()
    totalTime = endTime - startTime
    print(totalTime)

if __name__ == "__main__":
    main()