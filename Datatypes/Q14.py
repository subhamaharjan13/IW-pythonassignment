# Write a Python function to create the HTML string with tags around the word(s).

def tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)

print("'" + tags('i', 'Python') + "'")
print("'" + tags('b', 'Python Tutorial') + "'")