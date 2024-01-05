import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
#from scipy.stats import chi2_contingency 


# In[211]:


df1 = pd.read_csv("churn-bigml-80.csv")
df.head()


# In[212]:


df2 = pd.read_csv("churn-bigml-20.csv")
df.head()


# In[213]:


df1.shape


# In[214]:


df2.shape


# In[215]:


df = pd.concat([df1,df2], axis = 0)
df.head()


# In[216]:


df.shape


# In[31]:


df.info()


# In[32]:


df.isnull().sum()


# In[33]:


df.describe()


# In[136]:


df.describe(include=["object"]).T


# In[60]:


churn =df['Churn'].value_counts()
churn


# In[160]:


plt.pie(churn,labels=labels,autopct='%1.1f%%')
plt.title('Overall Count of Churn')
plt.legend()
plt.show()
