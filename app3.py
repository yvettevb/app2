#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install opendatasets')


# In[3]:


pip install pandas


# In[8]:


import opendatasets as od
import pandas as pds


# In[9]:


od.download("https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents")


# In[ ]:


#"username":"yvette217","key":"58a06162115cd9d7b8e00f55ff1b946f"


# In[10]:


file = ('US_Accidents_Dec21_updated.csv')
newData = pds.read_csv(file)
newData.head()


# In[ ]:




