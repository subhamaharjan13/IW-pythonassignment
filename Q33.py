# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys

start = 1
end = 15

data = dict()
for n in range(start, end+1):
    data[n] = n*n


print(data)