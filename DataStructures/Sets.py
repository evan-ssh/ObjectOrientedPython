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


setA = {1, 2, 3}
setB = {3, 4, 5}
unionSet = setA.union(setB)
intersectSet = setA.intersection(setB)
differenceSet = setA.difference(setB)
print("Union:", setA | setB) #Returns elements in both sets
print("Union:", unionSet)
print("Intersection:", setA & setB) #Returns matching elements 
print("Intersection:", intersectSet)
print("Difference:", setA - setB) # Returns only whats not in set B from Set a
print("Difference:", differenceSet)
