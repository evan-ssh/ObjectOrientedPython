import random,csv,time
def mergeSort(arr):
    if len(arr) > 1:
        leftArr = arr[:len(arr)//2]
        righArr = arr[len(arr)//2:]

        mergeSort(leftArr)
        mergeSort(righArr)

        i = 0
        j = 0
        k = 0

        while i < len(leftArr) and j < len(righArr):
            if leftArr[i] < righArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = righArr[j]
                j += 1
            k += 1

        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(righArr):
            arr[k] = righArr[j]
            j += 1
            k += 1

def main():
    arr = []
    for _ in range(2000):
        arr.append(random.randint(1,100))
    startTime = time.time()
    mergeSort(arr)
    endTime = time.time()
    totalTime = endTime - startTime
    print(totalTime)

if __name__ == "__main__":
    main()