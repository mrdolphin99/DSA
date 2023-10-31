'''##### 1.
Define a function to count the frequency of words in a given list of words.

Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 
Output:

 {'apple': 3, 'orange': 2, 'banana': 1}
'''
#Time : O(n) == space
def count_word(words):
    word_w_count = {}
    for word in words:
        word_w_count[word] = word_w_count.get(word,0) + 1
    return word_w_count

'''##### 2.
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

Example:

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)
Output:

{'a': 1, 'b': 5, 'c': 7, 'd': 5}
'''
#Time complexity : O(n x m)
def merge_dict(dict1, dict2):
    new_dict = dict1.copy() # -----------> O(n)
    for key, value in dict2.items(): #------>O(m)
        new_dict[key] = new_dict.get(key,0) + value
    
    return new_dict

'''##### 3.
Key with the Highest Value
Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

Example:

my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict))
Output:

b
'''

def highest_value(my_dict):
    return max(my_dict, key=my_dict.get)

'''##### 4.
Reverse Key-Value Pairs
Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.

Example:

my_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict(my_dict)
Output:

{1: 'a', 2: 'b', 3: 'c'}
'''

def reverse_dict(my_dict):
    return {value:key for key,value in my_dict.items()}
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))