#!/usr/bin/env python
# coding: utf-8

# In[40]:


get_ipython().system('pip install opendatasets')
get_ipython().system('pip install opendatasets')


# In[41]:


import opendatasets as od 


# In[42]:


od.download('https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents?resource=download')


# In[43]:


import streamlit as st
import pandas as pd 
import numpy as np 


# In[ ]:


covid = pd.read_csv('US_Accidents_Dec21_updated.csv')


# In[ ]:


st.title('Accident database')


# In[ ]:


#Inputaccident = st.sidebar.selectbox('Severity', (1,2,3,4))


# In[ ]:


#Accidentselect = covid[covid['Severity'] == Inputaccident]


# In[ ]:


#st.dataframe(Accidentselect)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




