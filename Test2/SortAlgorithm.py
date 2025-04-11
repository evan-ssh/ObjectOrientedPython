import time


 #o(n^2) everytime a pass is made it must be compared then swapped causing it to increase quadratically unless array is already sorted which would be linear
def sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Forward pass
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        end -= 1  # Reduce the effective range

        if not swapped:
            break  # If no swaps happened, array is already sorted

        swapped = False

        # Backward pass
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1  # Increase the effective range



def main():
    values = [5, 3, 8, 6, 2]
    start = time.time()
    sort(values)
    end = time.time() 
    print(values)



if __name__ == "__main__":
    main()