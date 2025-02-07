from randintlist import RandomIntList

def main():
    while True:
        print("Random Integer List")
        try:
            number_of_ints = int(input("\nHow many random integers should the list contain?: "))
            if number_of_ints < 0:
                print("\nEnter a positive number")
                continue
            randlist = RandomIntList(number_of_ints)
        except ValueError:
            print("\nEnter a valid number")
            continue
        
        print("\nRandom Integers\n" + '='*15)
        print(f"Integers: {randlist}")
        print(f"Count: {randlist.count()}")
        print(f"Total: {randlist.totalSum()}")
        print(f"Average: {randlist.average()}")
        go_again = input("\nContinue? (y/n): ")
        if go_again.lower() != "y":
            print("Bye!")
            break

if __name__ == "__main__":
    main()