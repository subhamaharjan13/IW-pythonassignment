# Write a binary search function. It should take a sorted sequence and the item it is looking for. 
# It should return the index of the item if found. It should return -1 if the item is not found.

def binarySearch(list, start, stop, item):
    while start <= stop:
        mid = start + (stop - start)
        # Check if x is present at mid 
        if list[mid] == item:                     
            return mid
        # If x is greater, ignore left half 
        elif list[mid] < item:                   
            start = mid + 1
        # If x is smaller, ignore right half 
        else:                                     
            stop = mid - 1
    # If we reach here, then the element was not present 
    return -1                                     

numbers = [0,99,2,6,4,8,12,13,17,15]
item = 99
  
result = binarySearch(sorted(numbers), 0, len(numbers)-1, item) 
  
if result != -1: 
    print("Element is present at index % d" %result) 
else: 
    print("Element is not present in list") 