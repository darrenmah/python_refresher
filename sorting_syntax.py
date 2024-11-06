elements = [5,4,1,2,3]
#Sort Ascending
elements.sort()
print(elements)

#Reverse Sorting (Descending)
elements.sort(reverse = True)
print(elements)

#Custom Sort using Key, Key takes in a function that will return a value to be used for sorting

def get_word_len(word):
    return len(word)

words = ['these','are','a','set','of','words']
words.sort(key = get_word_len)
print(words)

#Sort Lambda - Instead of defining a separate function to pass as a key, we can use lambdas
words.sort(key= lambda word: len(word))

#Sorted Copy
words = ['Z','B','A','C','E','D']
new_words = sorted(words)
print(words)
print(new_words)
