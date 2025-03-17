leftList = [2,3,1,6,1,3,4,1,2]
rightList = [4,14,2,5,3]
def merge(leftList,rightList):
    leftIndex = 0
    rightIndex = 0
    mergeList = []
    while leftIndex < len(leftList) and rightIndex < len(rightList):
        if leftList[leftIndex] < rightList[rightIndex]:
            mergeList.append(leftList[leftIndex])
            leftIndex += 1
        else:
            mergeList.append(rightList[rightIndex])
            rightIndex += 1
    mergeList.extend(leftList[leftIndex:])
    mergeList.extend(rightList[rightIndex:])
    return mergeList


def mergeSort(leftList,rightList):
    pass

mergedList = merge(leftList,rightList)