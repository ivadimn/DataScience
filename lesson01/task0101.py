#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


a = np.array([[1, 6],
             [2, 8],
             [3, 11],
             [3, 10],
             [1, 7]])


# In[9]:


mean_a = np.mean(a, axis=0)


# In[10]:


mean_a


# In[11]:


a_centered = a - mean_a


# In[12]:


a_centered


# In[ ]:




