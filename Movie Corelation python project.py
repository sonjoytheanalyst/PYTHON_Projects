#!/usr/bin/env python
# coding: utf-8

# In[2]:


# First let's import the packages we will use in this project
# You can do this all now or as you need them
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None


# Now we need to read in the data
df=pd.read_csv(r'C:\Users\FC\Downloads\movies.csv')


# In[7]:


# Now let's take a look at the data

df.head()


# In[8]:


# We need to see if we have any missing data
# Let's loop through the data and see if there is anything missing

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# In[9]:


# Data Types for our columns

print(df.dtypes)


# In[11]:


# Change data type of coloum
df['budget']=df['budget'].astype('int64')
df['gross']=df['gross'].astype('int64')


# In[12]:


df


# In[10]:


# Are there any Outliers?

df['yearcorrect']=df['released'].astype(str).str[:4]
df


# In[13]:


df = df.sort_values(by=['gross'],inplace=False, ascending=False)


# In[12]:


pd.set_option('display.max_rows',None)


# In[18]:


#Drop any Duplicate
df['company'].drop_duplicates().sort_values(ascending=False)


# In[16]:


df.drop_duplicates()


# In[17]:


df


# In[ ]:


# Budget High correlation
# Company High correlation


# In[25]:


#scater plot with budget vs gross
plt.scatter(x=df['budget'],y=df['gross'])
plt.title('Budget vs Gross Earnings')
plt.xlabel('Gross earnings')
plt.ylabel('Budget for Flim')
plt.show


# In[24]:


df.head()


# In[27]:


#plot budget vs gross using seaborn

sns.regplot(x='budget', y='gross',data=df,scatter_kws={"color":"red"},line_kws={"color":"blue"})


# In[29]:


#lets start looking at co relation

df.corr(method='pearson')  # Others method are kendall,spearman


# In[33]:



# high correlation between budget vs gross

correlation_matrix = df.corr(method='pearson')

sns.heatmap(correlation_matrix, annot=True)
plt.title('correlation matrix for numeric features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()


# In[34]:


# Looks at company
df.head()


# In[4]:


df_numerized=df
for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype=='object'):
        df_numerized[col_name] = df_numerized[col_name].astype('category')
        df_numerized[col_name]=df_numerized[col_name].cat.codes
        
    df_numerized
        


# In[5]:


df


# In[6]:


correlation_matrix = df_numerized.corr(method='pearson')

sns.heatmap(correlation_matrix, annot=True)
plt.title('correlation matrix for numeric features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()


# In[7]:


df_numerized.corr()


# In[8]:


correlation_mat=df_numerized.corr()
corr_pairs = correlation_mat.unstack()
corr_pairs 


# In[9]:


sorted_pairs= corr_pairs .sort_values()
sorted_pairs


# In[10]:


high_corr = sorted_pairs[(sorted_pairs>0.5)]
high_corr


# In[11]:



sns.stripplot(x="rating", y="gross", data=df)


# In[ ]:





# In[ ]:




