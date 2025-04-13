import heapq

# Create an empty list to represent the heap
heap = []

# Add elements to the heap
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 1)

# Display the heap
print("Heap:", heap)

# Remove the smallest element from the heap
smallest = heapq.heappop(heap)
print("Removed smallest element:", smallest)

# Display the heap after removal
print("Heap after removal:", heap)

# Peek at the smallest element without removing it
print("Smallest element:", heap[0])