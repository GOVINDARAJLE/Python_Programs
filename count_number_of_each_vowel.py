# program to count the number of each vowel in a string

# string of vowels

# define a function for counting the number of each vowel
def count_vowels(string):
    """
    Count the number of each vowel in a string
    """
    # initialize a dictionary to store the number of each vowel
    vowel_count = {}
    # initialize a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    # iterate through the vowels
    for vowel in vowels:
        # count the number of each vowel in the string
        vowel_count[vowel] = string.count(vowel)
    # return the dictionary
    return vowel_count

# main program
# take string from user
string = input("Enter a string: ")
# call the function
vowel_count = count_vowels(string)
# print the dictionary
print(vowel_count)
