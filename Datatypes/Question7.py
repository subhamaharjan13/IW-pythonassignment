# Write a Python function that takes a list of words and returns the length of the longest one.

bag_of_words = ['python', 'function', 'that', 'takes', 'a', 'list', 'of', 'words', 'and', 'returns', 'the', 'length', 'of', 'the', 'longest', 'one']

longest_word = max(bag_of_words, key = len)
length = max(len(word) for word in bag_of_words)

print("The longest length in the list is: %s." %length)
print("The longest word in the list is: %s." %longest_word)