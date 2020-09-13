#!/usr/bin/env python
# coding: utf-8

# # Samruddhi Benkar - Assignment No 6

# ## Make a Function for prime numbers and use Filter to filter out all the prime numbers from 1-2500

# In[1]:


def checkPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
        else:
            return True

prime_no=filter(checkPrime, range(2500))

print ('Prime numbers between 1-2500 are:\n\n', list(prime_no))


# In[ ]:




