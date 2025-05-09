from collections import deque

class CallCenterQueue:
    def __init__(self):
        self.queue = deque()

    def add_caller(self, name):
        self.queue.append(name)

    def answer_call(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return None

    def peek(self):
        if self.queue:
            return self.queue[0]
        else:
            return None

    def show_callers(self):
        return list(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


def main():
    ccq = CallCenterQueue()

    while True:
        print("\n1. Add Caller")
        print("2. Answer Call")
        print("3. Show Waiting Callers")
        print("4. Peek at Next Caller")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter caller name: ")
            ccq.add_caller(name)
            print(f"{name} added to queue.")
        elif choice == "2":
            caller = ccq.answer_call()
            if caller:
                print(f"Answered call from {caller}.")
            else:
                print("No callers in queue.")
        elif choice == "3":
            callers = ccq.show_callers()
            print("Waiting callers:", callers)
        elif choice == "4":
            next_caller = ccq.peek()
            if next_caller:
                print(f"Next caller is: {next_caller}")
            else:
                print("Queue is empty.")
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
