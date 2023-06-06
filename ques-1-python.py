#!/usr/bin/env python
# coding: utf-8

# In[ ]:


“write write write all the number from from from 1 to 100”


# In[3]:


def get_highest_frequency_word_length(string):
    # Remove punctuation and convert string to lowercase
    string = ''.join(c.lower() for c in string if c.isalpha() or c.isspace())
    
    # Split the string into words
    words = string.split()
    
    # Count the frequency of each word
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Find the highest frequency
    max_frequency = 0
    for count in word_counts.values():
        if count > max_frequency:
            max_frequency = count
    
    # Find the length of the highest-frequency word
    max_frequency_word_length = 0
    for word, count in word_counts.items():
        if count == max_frequency and len(word) > max_frequency_word_length:
            max_frequency_word_length = len(word)
    
    return max_frequency_word_length

# Test the function
input_string = input("Enter a string: ")
result = get_highest_frequency_word_length(input_string)
print("Length of the highest-frequency word:", result)


# In[ ]:




