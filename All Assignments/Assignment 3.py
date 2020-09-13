#!/usr/bin/env python
# coding: utf-8

# # Samruddhi Benkar - Assignment No 3

# ## You all are Pilots, you want to land a plane safely, so w.a.p to take current altitude as input and check whether the altitude is less than 1000 ft. to land the plane, or more than 1000 ft, and if it's less than  5000 ft. ask pilot to bring it down to 1000 ft. and if its more than 5000 ft. then ask pilot to turn around and attempt later.

# In[1]:


current_altitude = int(input("Enter the current altitude : "))

if current_altitude<=1000:
    print("Safe to land.")
elif current_altitude>1000 and current_altitude<5000:
    print("Bring down to 1000 ft.")
else:
    print("Turn around and attempt later.")


# In[ ]:




