#!/usr/bin/env python
# coding: utf-8

# # Samruddhi Benkar - Assignment No 9

# ## For this challenge,create a cone class that has two attributes: r=Radius h=Height and two methods: Volume = Π * r2 = (h/3) and Surface area : base : Π * r2 , side : Π * r * √(r2 + h2). Make only one class with functions,as in where required import Math.

# In[1]:


import math

class Cone():
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height
    
    def Volume(self):
        volume = ((math.pi)*self.radius*self.radius)*(self.height/3)
        print("Volume of cone is: " , volume)
        
    def S_Area(self):
        base = ((math.pi)*(self.radius*self.radius))
        side = (((math.pi)*(self.radius))*(math.sqrt((self.height*self.height)+(self.radius*self.radius))))
        area = base + side
        print("Surface area of cone is: " , area)


# In[2]:


a = Cone(5,4)


# In[3]:


a.Volume()


# In[4]:


a.S_Area()


# In[ ]:




