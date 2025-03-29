numSet = {1,2,3}
numSet.add(4) #Add
numSet.add(2) # Doesn't get added since its a duplicate
print(numSet)

numSet.remove(1) #Remove from set
print(numSet)

numSet.discard(0) #Discard doesn't raise an error if its not in set unlike remove
print(numSet)

popItem = numSet.pop() #Removes and returns item
print(popItem)


