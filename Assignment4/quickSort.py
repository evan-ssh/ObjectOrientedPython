import csv, random, time

def quickSort(arr, left, right):
    stack = []
    stack.append((left, right))
    while stack:
        left, right = stack.pop()
        if left < right:
            partitionPosition = partition(arr, left, right)
            stack.append((left, partitionPosition - 1))
            stack.append((partitionPosition + 1, right))

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i

def main():
    arr = []
    for _ in range(2000):
        arr.append(random.randint(1,100))
    startTime = time.time()
    quickSort(arr, 0, len(arr) - 1)
    endTime = time.time()
    totalTime = endTime - startTime
    print(totalTime)
  

if __name__ == "__main__":
    main()