import heapq

def findNSmallest(nums, n):
    heapq.heapify(nums)
    nsmallest = [heapq.heappop(nums) for _ in range(n)]
    return nsmallest

nums = [10, 5, 20, 1, 15, 25, 8]
n= 3
print(f"The {n} smallest elements are: {findNSmallest(nums, n)}")