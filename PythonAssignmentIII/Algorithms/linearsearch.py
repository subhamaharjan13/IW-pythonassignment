def search(list, n, x): 
  
    for i in range (0, n): 
        if (list[i] == x): 
            return i
    return -1
  
data = [ 2, 3, 4, 10, 40 ]
x = 40
n = len(data)
result = search(data, n, x) 
if(result == -1): 
    print("Element is not present in list") 
else: 
    print("Element is present at index", result)