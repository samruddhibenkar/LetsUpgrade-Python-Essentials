#!/usr/bin/env python
# coding: utf-8

# # Samruddhi Benkar - Assignment No 5

# ## Write a program to identify sub list [1,1,5] is there in the given list in the same order, if yes print “it’s a Match” if no then print “it’s Gone” in function.

# In[2]:


x = [1,5,6,4,1,2,3,5]
y = [1,1,5]

def check(a,b):
    for i in a:
        for j in b:
            if(len(b)>=0 and j == i):
                b.pop(0)
            else:
                break
    return b

if len(check(x,y))==0:
    print("It's a Match")
else: print("It's Gone")

check(x,y)


# In[3]:


x = [1,5,6,5,1,2,3,6]
y = [1,1,5]

def check(a,b):
    for i in a:
        for j in b:
            if(len(b)>=0 and j == i):
                b.pop(0)
            else:
                break
    return b

if len(check(x,y))==0:
    print("It's a Match")
else: print("It's Gone")

check(x,y)


# In[ ]:




