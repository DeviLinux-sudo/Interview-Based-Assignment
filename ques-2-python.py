#!/usr/bin/env python
# coding: utf-8

# In[13]:


def is_valid_string(s):
   
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
   
    frequencies = set(char_counts.values())
    max_frequency = max(frequencies)
    
   
    count_max_frequency = sum(1 for count in char_counts.values() if count == max_frequency)
    
   
    if len(frequencies) == 1:
        return "YES"
    
    elif len(frequencies) == 2 and count_max_frequency == 1 and (max_frequency - 1 == min(frequencies) or min(frequencies) == 1):
        return "YES"

    else:
        return "NO"


input_string_1 = "abc"
result_1 = is_valid_string(input_string_1)
print("Input 1:", input_string_1)
print("Output 1:", result_1)


input_string_2 = "abcc"
result_2 = is_valid_string(input_string_2)
print("Input 2:", input_string_2)
print("Output 2:", result_2)


input_string_3 = "aabbbbcc"
result_3 = is_valid_string(input_string_3)
print("Input 3:", input_string_3)
print("Output 3:", result_3)


# In[ ]:




