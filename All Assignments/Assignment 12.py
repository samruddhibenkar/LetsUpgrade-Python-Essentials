#!/usr/bin/env python
# coding: utf-8

# # Samruddhi Benkar - Assignment No 12

# ## Write a python Function for finding is a given number prime or not and do Unit Testing on it using PyLint and Unittest Library.

# ## 1. PyLint

# In[1]:


get_ipython().system(' pip install pylint')


# In[2]:


get_ipython().run_cell_magic('writefile', 'check_prime_one.py', '\'\'\'\nCode to check whether a number is prime or not\n\'\'\'\ndef check_one():\n    \'\'\'To check whether prime or not\'\'\'\n    num = int(input("Enter Number to check - "))\n    if num > 1:\n        for i in range(2, num):\n            if (num % i) == 0:\n                print(num, "is not a prime number")\n                break\n        else:\n            print(num, "is a prime number")')


# In[3]:


get_ipython().system(' pylint "check_prime_one.py"')


# In[4]:


import check_prime_one

check_prime_one.check_one()


# In[5]:


import check_prime_one

check_prime_one.check_one()


# ## Unittest

# In[ ]:


get_ipython().system(' pip install unittest2')


# In[6]:


get_ipython().run_cell_magic('writefile', 'check_prime_two.py', 'def check_two(num):\n    if num > 1:\n        for i in range(2, num):\n            if(num % i) == 0:\n                return "not prime"\n                break\n        else:\n            return "prime"')


# In[7]:


import check_prime_two

check_prime_two.check_two(3)


# In[8]:


import check_prime_two

check_prime_two.check_two(15)


# In[9]:


get_ipython().run_cell_magic('writefile', 'testPrime.py', '\nimport unittest\nimport check_prime_two\n\nclass testP(unittest.TestCase):\n    def test_for_no1(self):\n        self.assertEqual(check_prime_two.check_two(15),"not prime")\n\n    def test_for_no2(self):\n        self.assertEqual(check_prime_two.check_two(3),"prime")\n        \nif __name__ == "__main__":\n    unittest.main()')


# In[10]:


get_ipython().system(' python testPrime.py')


# In[ ]:




