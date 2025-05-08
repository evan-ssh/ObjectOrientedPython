from collections import deque

def interleave_queue(q):
    n = len(q) // 2
    stack = []

    for _ in range(n):
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())
    for _ in range(n):
        q.append(q.popleft())
    for _ in range(n):
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())
        q.append(q.popleft())
    return list(q)

def main():
    q = deque([1, 2, 3, 4, 5, 6])
    print("Original queue:", list(q))
    print("Interleaved queue:", interleave_queue(q))

if __name__ == "__main__":
    main()