import heapq

def nLargestElements(nums, n):
    return heapq.nlargest(n, nums)

def main():
    nums = [10, 4, 7, 2, 15, 3, 8]
    n = int(input("How many elements to search for"))
    print(f"The {n} largest elements are:", nLargestElements(nums, n))

if __name__ == "__main__":
    main()