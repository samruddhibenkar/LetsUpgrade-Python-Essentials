#!/usr/bin/env python
# coding: utf-8

# # Samruddhi Benkar - Assignment No 10

# ## Write a decorator function for your taking input for you any kind of function you want to build, For example - You make a fibonacci series function,in which your input range is been defined by the decorator program input.

# In[1]:


def getInput(calculator_functn):
    def wrap_function():
        print("Welcome to my calculator!")
        num1 = int(input("Enter first number - "))
        num2 = int(input("Enter second number - "))    
        calculator_functn(num1, num2)
    return wrap_function


# In[2]:


@getInput

def addition(num1, num2):
    print("Addition is", num1 + num2)


# In[3]:


@getInput

def subtraction(num1, num2):
    print("Subtraction is", num1 - num2)


# In[4]:


@getInput

def division(num1, num2):
    print("Division is", num1 / num2)


# In[5]:


@getInput

def multiplication(num1, num2):
    print("Multiplication is", num1 * num2)


# In[6]:


addition()


# In[7]:


subtraction()


# In[8]:


division()


# In[9]:


multiplication()


# In[ ]:




