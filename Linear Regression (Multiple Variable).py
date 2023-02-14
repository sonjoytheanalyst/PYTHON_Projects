#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from sklearn import linear_model


# In[6]:


df = pd.read_csv(r"G:\CYBER SECURITY ALL MODULES\3rd SEMESTER\Data..csv")


# In[7]:


df


# In[11]:


mean_height = df.height.mean()


# In[12]:


df.height


# In[15]:


df.height=df.height.fillna(mean_height)


# In[16]:


df


# In[17]:


reg = linear_model.LinearRegression()


# In[19]:


reg.fit(df[['Age','height','weight']],df['Salary'])


# In[20]:


reg.coef_


# In[22]:


reg.intercept_


# In[23]:


reg.predict([[27,167.56,60]])


# In[24]:


2150.26052416*27+-248.45851574*167.56+312.65291961*60+-16827.013154824977


# In[25]:


reg.predict([[60,165.10,80]])


# In[26]:


2150.26052416*60+-248.45851574*165.10+312.65291961*80+-16827.013154824977


# In[ ]:




