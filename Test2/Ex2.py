from DataStructures import Stack,Queue


def serveCustomer(console, customer):
    stack = Stack()
    queue = Queue()

    for char in console:
        stack.push(char)
    for cust in customer:
        queue.enqueue(cust)

    while not queue.isEmpty() and not stack.isEmpty():
        served = False
        for _ in range(queue.size()):
            if queue.peek() == stack.peek():
                queue.dequeue()
                stack.pop()
                served = True
                break
            else:
                queue.enqueue(queue.dequeue())
        if not served:
            break

    return queue.size()
def main():
    console = ['X','X','X','P','P','X','P','X','P','X','P','P','P']
    customers = ['X','P','X','P','P','X','X','P','P','X','X','X','X']
    unable_to_buy = serveCustomer(console,customers)
    print(f"There are {unable_to_buy} customer(s) who were unable to purchase a console")
if __name__ == "__main__":
    main()