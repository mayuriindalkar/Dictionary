# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}


str1='w3resource' 
my_dict={}
for letter in str1:
    my_dict[letter]=my_dict.get(letter,0)+1
print(my_dict)