#!/usr/bin/env python
# coding: utf-8

# # Samruddhi Benkar - Assignment No 2

# ## Using for loop please print all the prime numbers between 1 - 200 using FOR LOOP and RANGE function

# In[1]:


for no in range(1,200):
    if no > 1:
        for i in range(2,no):
            if (no % i) == 0:
                break  
        else:
            print(no)


# In[ ]:




