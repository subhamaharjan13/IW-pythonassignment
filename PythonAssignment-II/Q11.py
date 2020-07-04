# Create a variable, filename. Assuming that it has a three-letter extension, and using slice operations, find the extension. 
# For README.txt, the extension should be txt. Write code using slice operations that will give the name without the extension. 
# Does your code work on filenames of arbitrary length?

filename = "README.txt"

# using slice operation to print the extension of file and the file name without extension
print("File name = {} \nThe extension is = {} \nFilename Without Extension = {}"
            .format(filename,filename[filename.index('.')+1:],filename[0:filename.index('.')]))