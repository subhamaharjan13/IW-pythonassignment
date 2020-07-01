# Write a Python function that takes a list of words and returns the length of the longest one.

bag_of_words = ['python', 'function', 'that', 'takes', 'a', 'list', 'of', 'words', 'and', 'returns', 'the', 'length', 'of', 'the', 'longest', 'one']

print("The longest word in the list is:", max(bag_of_words, key = len))
print("The longest length in the list is: ", max(len(word) for word in bag_of_words))