# Write a Python program to print the even numbers from a given list.

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result_list = []

def even(list):
    for i in list:
        if i % 2 == 0:
            result_list.append(i)

    return result_list

print(even(sample_list))