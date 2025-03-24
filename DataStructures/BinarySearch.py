def BinarySearch(arr, item):
    begin_index = 0 
    end_index = len(arr) - 1 

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = arr[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1 

        else:
            begin_index = midpoint + 1
    return None

if __name__ == "__main__":
    arr = [2,3,4,5,6]
    item = 4
    print(BinarySearch(arr,item))