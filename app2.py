#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install opendatasets')


# In[2]:


import opendatasets as od 


# In[5]:


od.download('https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents?resource=download')


# In[6]:


import streamlit as st
import pandas as pd 
import numpy as np 


# In[7]:


covid = pd.read_csv('US_Accidents_Dec21_updated.csv')


# In[8]:


st.title('Accident database')


# In[9]:


Inputaccident = st.sidebar.selectbox('Severity', (1,2,3,4))


# In[11]:


Accidentselect = covid[covid['Severity'] == Inputaccident]


# In[12]:


st.dataframe(Accidentselect)


# In[ ]:




