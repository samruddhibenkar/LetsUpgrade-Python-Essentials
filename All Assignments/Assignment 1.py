#!/usr/bin/env python
# coding: utf-8

# # Samruddhi Benkar - Assignment No 1
# 

# ## Que 1: List and its default functions.

# In[1]:


myList = ["Apple", "Banana", "Coconut", "Dragonfruit", "Elderberry", "Fig"]  #My List


# In[2]:


myList


# In[3]:


myList.append("Grapes")  #1. append()


# In[4]:


myList


# In[5]:


myList.clear()  #2. clear()


# In[6]:


myList


# In[7]:


myList = ["Apple", "Banana", "Coconut", "Dragonfruit", "Elderberry", "Banana"]


# In[8]:


myList


# In[9]:


myList.count("Banana")  #3. count()


# In[10]:


myList.index("Coconut")  #4. index()


# In[11]:


myList.pop()  #5. pop()


# In[12]:


myList


# In[13]:


myList.reverse()  #6. reverse


# In[14]:


myList


# In[15]:


myList.sort()  #7. sort()


# In[16]:


myList


# In[18]:


myList.insert(5, "Fig")  #8. insert()


# In[19]:


myList


# In[20]:


myList.remove("Coconut")   #9. remove()


# In[21]:


myList


# ## Que 2: Dictionary and its default functions.

# In[22]:


myDictn = {'fname':'Samruddhi', 'lname':'Benkar', 'age':'22', 'city':'Satara'}   #My Dictionary


# In[23]:


myDictn


# In[24]:


myDictn.get('age')   #1. get()


# In[25]:


myDictn.items()   #2. items()


# In[26]:


myDictn.keys()   #3. keys()


# In[27]:


myDictn.pop('age')   #4. pop()


# In[28]:


myDictn


# In[29]:


myDictn.clear()   #5. clear()


# In[30]:


myDictn


# ## Que 3: Set and its default functions.

# In[31]:


mySet = {'Samruddhi', 'Benkar', 22, 'Satara', 55.0, 'Panda'}   #My Set


# In[32]:


mySet


# In[33]:


mySet.add('Purple')   #1. add()


# In[34]:


mySet


# In[35]:


mySet.discard(55.0)   #2. discard()


# In[36]:


mySet


# In[37]:


newSet = {'Samruddhi', 'Benkar', 'Rabbit', 3198}   #New Set


# In[38]:


newSet


# In[39]:


mySet.difference(newSet)   #3. difference()


# In[40]:


mySet.union(newSet)   #4. union()


# In[41]:


mySet.pop()   #5. pop()


# In[42]:


mySet


# In[43]:


mySet.remove(22)   #6. remove()


# In[44]:


mySet


# In[45]:


mySet.clear()   #7. clear()


# In[46]:


mySet


# ## Que 4: Tuple and its default functions.

# In[47]:


myTuple = ('Samruddhi', [3, 1, 98], 'Benkar', 3198, [1, 2, 3])   #My Tuple


# In[48]:


myTuple


# In[51]:


myTuple.count(3198)   #1. count()


# In[52]:


myTuple.index(3198)   #2. index()


# ## Que 5: String and its default functions.

# In[54]:


firstname = 'samruddhi'


# In[55]:


middlename = 'Pramod'


# In[56]:


lastname = 'Benkar'


# In[57]:


firstname.capitalize()   #1. capitalize()


# In[58]:


middlename.casefold()   #2. casefold()


# In[59]:


firstname.count('d')   #3. count()


# In[60]:


lastname.find('a')   #4. find()


# In[62]:


firstname.index('m')   #5. index()


# In[63]:


lastname.isalpha()   #6. isalpha()


# In[64]:


middlename.isdigit()   #7. isdigit()


# In[ ]:




