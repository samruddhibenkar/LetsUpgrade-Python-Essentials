#!/usr/bin/env python
# coding: utf-8

# # Samruddhi Benkar - Assignment No 13

# ## Make a small generator program for returning armstrong numbers in between 1-1000 in a generator object.

# In[1]:


lst = list(range(1000))


# In[2]:


def getArmstrongNumber(lst):
    for num in lst:
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if num == sum:
            yield num


# In[3]:


print(list(getArmstrongNumber(lst)))


# In[ ]:




