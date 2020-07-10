def interpolationSearch(list, n, x): 
    # Find indexs of two corners 
    low = 0
    high = (n - 1) 
   
    # Since list is sorted, an element present 
    # in list must be in range defined by corner 
    while(low <= high and x >= list[low] and x <= list[high]): 
        if low == high: 
            if list[low] == x:  
                return low 
            return -1
          
        # Probing the position with keeping 
        # uniform distribution in mind. 
        pos  = low + int(((float(high - low) / 
            ( list[high] - list[low])) * ( x - list[low]))) 
  
        # Condition of target found 
        if list[pos] == x: 
            return pos 
   
        # If x is larger, x is in upper part 
        if list[pos] < x: 
            low = pos + 1
   
        # If x is smaller, x is in lower part 
        else: 
            high = pos - 1
      
    return -1
  

data = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47] 
n = len(data) 
  
print("Sorted list is:", sorted(data))
x = 18 # Element to be searched 
index = interpolationSearch(data, n, x) 
  
if index != -1: 
    print("Element found at index",index)
else: 
    print("Element not found")