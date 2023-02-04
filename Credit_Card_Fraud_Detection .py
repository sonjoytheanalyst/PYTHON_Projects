#!/usr/bin/env python
# coding: utf-8

# # IMPORT ALL DEPENDENCIES

# In[1]:


import numpy as np #Useful for making Arrays
import pandas as pd # Useful for CSV file and it works with dataframe
from sklearn.model_selection import train_test_split #Useful for training and testing data
from sklearn.linear_model import LogisticRegression #Useful for checking accuracy of the model
from sklearn.metrics import accuracy_score # Useful for checking the performance of the model


# # Loading dataset of CSV file using pandas function

# In[2]:


credit_card_data=pd.read_csv(r"G:\Project 4 Python\Credit Card Fraud detection\creditcard.csv")


# #  first 5 rows of the dataset

# In[3]:


credit_card_data.head()


# # Last 5 rows of the dataset

# In[4]:


credit_card_data.tail()


# # dataset informations

# In[5]:


credit_card_data.info()


# # checking the number of missing values in each column

# In[11]:


credit_card_data.isnull().sum()


# # Distribuation of legit and fradulant transaction

# In[14]:


credit_card_data['Class'].value_counts()


# This Dataset is highly unblanced
# 
# 0 --> Normal Transaction
# 
# 1 --> fraudulent transaction

# # separating the data for analysis

# In[15]:


legit=credit_card_data[credit_card_data.Class==0]
fraud=credit_card_data[credit_card_data.Class==1]


# In[16]:


print(legit.shape)
print(fraud.shape)


# # statistical measures of the data

# In[17]:


credit_card_data.describe()


# In[19]:


legit.Amount.describe()


# In[18]:


fraud.Amount.describe()


# # compare the values for both transactions

# In[20]:


credit_card_data.groupby('Class').mean()


# Under-Sampling
# 
# Build a sample dataset containing similar distribution of normal transactions and Fraudulent Transactions
# 
# Number of Fraudulent Transactions --> 492
# 
# 

# In[35]:


legit_sample=legit.sample(n=600)


# Concatenating two DataFrames

# In[36]:


new_dataset = pd.concat([legit_sample,fraud],axis=0)


# In[37]:


new_dataset.head()


# In[38]:


new_dataset.tail()


# In[39]:


new_dataset['Class'].value_counts()


# In[40]:


new_dataset.groupby('Class').mean()


# ## Splitting the data into Features & Targets

# In[41]:


X= new_dataset.drop(columns='Class',axis=1)
Y = new_dataset['Class']


# In[29]:


print(X)


# In[42]:


print(Y)


# ## Split the data into Training data & Testing Data

# In[43]:


X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y, random_state=2)


# In[44]:


print(X.shape,X_train.shape,X_test.shape)


# In[45]:


print(Y.shape,Y_train.shape,Y_test.shape)


# ## Model Training || Logistic Regression

# In[46]:


model= LogisticRegression()


# ## Training the logistic regression model with training data

# In[49]:


model.fit(X_train, Y_train)


# In[50]:


X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)


# In[51]:


print('Accuracy on Training data : ', training_data_accuracy)


# In[52]:


# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)


# In[53]:


print('Accuracy score on Test Data : ', test_data_accuracy)


# In[ ]:




