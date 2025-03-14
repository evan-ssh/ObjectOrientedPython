leftList = [1,2,3,2]
rightList = [2,4,6]


def mergeSort(leftList,rightList):
    leftindex = 0
    rightindex = 0
    mergeList = []
    while leftindex < len(leftList)  and rightindex < len(rightList):
        if leftList[leftindex] < rightList[rightindex]:
            mergeList.append(leftList[leftindex])
            leftindex += 1
        else:
            mergeList.append(rightList[rightindex])
            rightindex += 1

    while leftindex < len(leftList):
        mergeList.append(leftList[leftindex])
        leftindex += 1

    while rightindex < len(rightList):
        mergeList.append(rightList[rightindex])
        rightindex += 1

    return mergeList

print(mergeSort(leftList,rightList))