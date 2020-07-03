# Write code that will print out the anagrams (words that use the same letters) from a paragraph of text.

from collections import defaultdict  
  
def printAnagrams(words): 
    groupedWords = defaultdict(list) 
  
    # Put all anagram words together in a dictionary  
    for word in words: 
        groupedWords["".join(sorted(word))].append(word) 
  
    # Print all anagrams together 
    for group in groupedWords.values(): 
        print(" ".join(group))       
  
  
if __name__ == "__main__":    
    anagramlist =  ["cat", "dog", "stop","tac", "desserts","god", "act","stressed","pots"]   
    printAnagrams(anagramlist)