#!/usr/bin/env python
# coding: utf-8

# # Samruddhi Benkar - Assignment No 7

# ## Make a Lambda function for capitalizing the whole sentence passed using arguments and map all the sentences in the List, with the lambda functions.

# In[1]:


myList = ["hi, i am samruddhi benkar."]

capital = map(lambda a: a.title(), myList)
print(list(capital))


# In[ ]:




