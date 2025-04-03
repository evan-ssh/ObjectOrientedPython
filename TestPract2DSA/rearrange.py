def interleaveQueue(queue):
    if len(queue) % 2 != 0:
        print("Queue length must be even.")
        return queue

    stack = Stack()
    half = len(queue) // 2

    # Step 1: Push the first half of the queue into the stack
    for _ in range(half):
        stack.push(queue.pop())

    # Step 2: Enqueue the elements from the stack back into the queue
    while len(stack.stack) > 0:
        queue.enqueue(stack.pop())

    # Step 3: Move the first half of the queue to the back
    for _ in range(half):
        queue.enqueue(queue.pop())

    # Step 4: Push the first half of the queue into the stack again
    for _ in range(half):
        stack.push(queue.pop())

    # Step 5: Interleave the elements from the stack and the queue
    while len(stack.stack) > 0:
        queue.enqueue(stack.pop())  # Add one element from the stack
        queue.enqueue(queue.pop())  # Add one element from the queue

    return queue

def main():
    queue = Queue()
    for i in [1, 2, 3, 4, 5, 6]:
        queue.enqueue(i)

    print("Original Queue:", queue.display())
    interleaveQueue(queue)
    print("Interleaved Queue:", queue.display())

if __name__ == "__main__":
    main()