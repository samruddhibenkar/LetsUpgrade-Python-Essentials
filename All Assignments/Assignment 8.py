#!/usr/bin/env python
# coding: utf-8

# # Samruddhi Benkar - Assignment No 8

# ## For this challenge, create a bank account class that has two attributes: ownerName and balance and two methods deposit and draw. As an added requirement,withdrawals may not exceed the available balance. Instantiate your class, take several deposits and withdrawals, and test to make sure the account cant be overdrawn.

# In[1]:


class Bank_Account: 
    def __init__(self,ownerName): 
        self.balance = 0
        self.ownerName = ownerName
        print("Hello",str(self.ownerName) , "Welcome to the Deposit & Withdrawal Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 


# In[2]:


s = Bank_Account("Samruddhi")


# In[3]:


s.deposit()


# In[4]:


s.withdraw()


# In[5]:


s.deposit()


# In[6]:


s.display()


# In[ ]:




