from collections import deque
class CallCenterQueue:
    def __init__(self):
        self.queue = deque()

    def add_caller(self, name, vip=False):
        if vip:
            self.queue.appendleft((name, True))
        else:
            self.queue.append((name, False))

    def answer_call(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return None
        
    def clear_queue(self):
        self.queue.clear()

    def peek(self):
        if self.queue:
            return self.queue[0]
        else:
            return None

    def show_callers(self):
        return list(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def remove_caller(self, name):
        for caller, (caller_name, vip) in enumerate(self.queue):
            if caller_name == name:
                del self.queue[caller]
                return True, vip
        return False, None

    def upgrade_to_vip(self, name):
        for caller, (caller_name, vip) in enumerate(self.queue):
            if caller_name == name:
                del self.queue[caller]
                self.queue.appendleft((name, True))
                return True, vip
        return False, None
    
    def find_caller_position(self, name):
        for caller, (caller_name, vip) in enumerate(self.queue):
            if caller_name == name:
                return caller + 1, vip
        return None, None

def main():
    ccq = CallCenterQueue()
    call_history = []  

    while True:
        print("\n1. Add Caller")
        print("2. Answer Call")
        print("3. Show Waiting Callers")
        print("4. Peek at Next Caller")
        print("5. Exit")
        print("6. Add VIP Caller")
        print("7. Remove Caller by Name")
        print("8. Show Last 5 Answered Calls")
        print("9. Show Caller Counts")
        print("10. Upgrade Caller to VIP")
        print("11. Find Caller Position")  
        print("12. Clear Queue")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter caller name: ")
            ccq.add_caller(name)
            print(f"{name} added to queue.")
        elif choice == "2":
            caller = ccq.answer_call()
            if caller:
                name, vip = caller
                status = " (VIP)" if vip else ""
                print(f"Answered call from {name}{status}.")
                call_history.append((name, vip))  
            else:
                print("No callers in queue.")
        elif choice == "3":
            callers = ccq.show_callers()
            if callers:
                print("Waiting callers:")
                for name, vip in callers:
                    status = " (VIP)" if vip else ""
                    print(f"- {name}{status}")
            else:
                print("No callers in queue.")
        elif choice == "4":
            next_caller = ccq.peek()
            if next_caller:
                name, vip = next_caller
                status = " (VIP)" if vip else ""
                print(f"Next caller is: {name}{status}")
            else:
                print("Queue is empty.")
        elif choice == "5":
            print("Exiting.")
            break
        elif choice == "6":
            name = input("Enter VIP caller name: ")
            ccq.add_caller(name, vip=True)
            print(f"{name} added to front of queue as VIP.")
        elif choice == "7":
            name = input("Enter the name of the caller to remove: ")
            removed, vip = ccq.remove_caller(name)
            if removed:
                status = " (VIP)" if vip else ""
                print(f"Removed {name}{status} from the queue.")
            else:
                print(f"No caller named {name} found in the queue.")
        elif choice == "8":
            print("Last 5 answered calls:")
            if call_history:
                for name, vip in reversed(call_history[-5:]):
                    status = " (VIP)" if vip else ""
                    print(f"- {name}{status}")
            else:
                print("No calls have been answered yet.")
        elif choice == "9":
            vip_count, regular_count = ccq.count_callers()
            total = vip_count + regular_count
            print(f"VIP callers: {vip_count}")
            print(f"Regular callers: {regular_count}")
            print(f"Total callers: {total}")
        elif choice == "10":
            name = input("Enter the name of the caller to upgrade to VIP: ")
            upgraded, was_vip = ccq.upgrade_to_vip(name)
            if upgraded:
                print(f"{name} has been moved to the front as a VIP!")
            else:
                print(f"No caller named {name} found in the queue.")
        elif choice == "11":
            name = input("Enter the name of the caller to find: ")
            position, vip = ccq.find_caller_position(name)
            if position:
                status = " (VIP)" if vip else ""
                print(f"{name}{status} is at position {position} in the queue.")
            else:
                print(f"No caller named {name} found in the queue.")
        elif choice == "12":
            ccq.clear_queue()
            print("All callers have been removed from the queue.")
        else:
            print("Invalid choice.")
        

if __name__ == "__main__":
    main()