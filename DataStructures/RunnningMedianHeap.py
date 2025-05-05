
import heapq

class MedianFinder:
    def __init__(self):
        self.low = []  
        self.high = []

    def add_num(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (-self.low[0] + self.high[0]) / 2

def main():
    mf = MedianFinder()
    nums = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    for num in nums:
        mf.add_num(num)
        print(f"Current median after adding {num}: {mf.find_median()}")

if __name__ == "__main__":
    main()