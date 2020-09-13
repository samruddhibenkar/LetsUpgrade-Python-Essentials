#!/usr/bin/env python
# coding: utf-8

# # Samruddhi Benkar - Assignment No 11

# ## For this challenge you need to develop a Python program to open a file in read only mode and try writing something to it and handle the subsequent errors using Exception Handling.

# In[1]:


try:
    f = open("File1.txt", "r")
    f.write("This is my text file for exception handling!!") 

except:
    print("Some unexpected error occurred")
    
    f.close()


# In[ ]:




