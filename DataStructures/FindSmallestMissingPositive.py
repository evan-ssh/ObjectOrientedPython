def MissingPositive(nums):
    num_set = set(nums)
    smallest = 1
    while smallest in num_set:
        smallest += 1
    return smallest

def main():
    nums = list(map(int, input("Enter a list of integers (space-separated): ").split()))
    result = MissingPositive(nums)
    print(f"The smallest missing positive integer is: {result}")

if __name__ == "__main__":
    main()