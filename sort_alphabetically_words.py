# program to sort words in alphabetical order

# take the input from the user
my_str = input("Enter a string: ")

# divide the string into words
words = my_str.split() 

# sort the words
words.sort()

# print the sorted words
print("The sorted words are:")
for word in words:
    print(word)
    