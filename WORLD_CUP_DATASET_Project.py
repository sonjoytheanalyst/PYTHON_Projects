#!/usr/bin/env python
# coding: utf-8

# In[1]:


# For manupulating
import pandas as pd
import numpy as np

# for data visualization
import seaborn as sns
import matplotlib.pyplot as plt

# for interactivity
from matplotlib.pyplot import figure
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')


# In[4]:


# Now we need to read in the data
fifa=pd.read_csv('wcmatches.csv')


# In[5]:


# It will print first 5 row of data
fifa.head()


# In[6]:


# For showing all the columns we will use for loop
for col in fifa.columns:
    print(col)


# In[7]:


# For showing all the row and columns in the dataset 
fifa.shape


# In[8]:


# For knowing which country played highest world cup matches
fifa['country'].value_counts()


# In[9]:


# For knowing Top 10 country who played highest world cup matches
fifa['country'].value_counts()[0:10]


# In[10]:


# For knowing Top 5 country who played highest world cup matches
fifa['country'].value_counts()[0:5]


# In[12]:


# Top five countries bar chart for that we need to extract each country value by using key function
fifa['country'].value_counts()[0:5].keys()


# In[13]:


# Bar chart for top five countries
plt.figure(figsize=(5,5))
plt.bar(list(fifa['country'].value_counts()[0:5].keys()),list(fifa['country'].value_counts()[0:5]),color="g")


# In[16]:


# by this command we weill find out all wining team and lossing teams in world cup
match_win=fifa[['winning_team','losing_team','home_score','date']]


# In[17]:


match_win.head()


# In[18]:


# Highest goal and winning teams from 1930 to 2018
match_win=match_win.sort_values(by=['home_score'],ascending=False)


# In[19]:


match_win.head()


# In[29]:


# we will make a bar chart by using this top five countries data
plt.figure(figsize=(9,6))
plt.bar(list(match_win['winning_team'])[0:7],list(match_win['home_score'])[0:7],color=["blue","green","orange","pink","red","yellow","black"])
plt.show()


# In[50]:


# For showing all top 10 matches organized country played between 1930 to 2018

Brazil=fifa[fifa['winning_team']=='Brazil']
Brazil=Brazil.sort_values(by=['year'],ascending =False)
Brazil.head(10)


# In[59]:


# Brazill all matches winning summary from 1930 to 2018
Brazil[['city','date','winning_team','losing_team','home_score']].sort_values(by=['date'],ascending =False).head(10)


# In[60]:



fifa.head(20)


# In[63]:


semi=fifa[fifa['stage']=='Final']
semi[['city','date','winning_team','stage']].sort_values(by=['date'],ascending =False).head(10)


# In[ ]:





# In[ ]:





# In[ ]:




