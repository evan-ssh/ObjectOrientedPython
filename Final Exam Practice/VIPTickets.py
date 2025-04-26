class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
def serveVIPTickets(tickets,people):
    stack = Stack()
    queue = Queue()
    for ticket in tickets:
        stack.push(ticket)
    for person in people:
        queue.enqueue(person)

    while not stack.isEmpty() and not queue.isEmpty():
        served = False
        for _ in range(queue.size()):
            ticket_number, is_vip = queue.peek()
            if is_vip and ticket_number == stack.peek():
                queue.dequeue()
                stack.pop()
                served = True
                break
            else:
                queue.enqueue(queue.dequeue())
        if not served:
            for _ in range(queue.size()):
                ticket_number, is_vip = queue.peek()
                if not is_vip and ticket_number == stack.peek():
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
    tickets = [101, 102, 103, 104]
    people = [(102, False), (104, True), (101, False), (103, False)]
    print("People unable to buy tickets:", serveVIPTickets(tickets, people))  # Output: 0

    tickets2 = [101, 102, 103, 104]
    people2 = [(105, False), (106, True), (107, False), (108, False)]
    print("People unable to buy tickets:", serveVIPTickets(tickets2, people2))  # Output: 4

if __name__ == "__main__":
    main()