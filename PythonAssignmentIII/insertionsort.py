def insertionSort(list): 
  
    # Traverse through 1 to len of list 
    for i in range(1, len(list)): 
  
        key = list[i] 
  
        # Move elements that are greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < list[j] : 
                list[j + 1] = list[j] 
                j -= 1
        list[j + 1] = key 
  
  
data = [12, 11, 13, 5, 6] 
insertionSort(data) 
for i in range(len(data)): 
    print (f"{data[i]}",end=" ") 