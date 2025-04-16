import heapq

def mergeLists(list1, list2):
    return list(heapq.merge(list1, list2))

def main():
    list1 = [1, 4, 7]
    list2 = [2, 3, 6]
    print( mergeLists(list1, list2)) 

if __name__ == "__main__":
    main()