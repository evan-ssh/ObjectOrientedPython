def bubbleSort(arr):
    for n in range(len(arr) - 1, 0, -1):
        swapped = False

        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

                swapped = True
        if not swapped:
            break

def main():
    arr = [5,1,7,3,8]
    bubbleSort(arr)
    print(arr)

if __name__ == "__main__":
    main()