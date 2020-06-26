# Write a Python program to find intersection of two given arrays using Lambda.

array1 = [2,4,6,8,0,11,13,16]
array2 = [1,3,7,9,11,13,15]

intersection = list(filter(lambda x: x in array1, array2))
print(intersection)