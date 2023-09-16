#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2023-01-01">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Exploratory Data Analysis Lab**
# 

# Estimated time needed: **30** minutes
# 

# In this module you get to work with the cleaned dataset from the previous module.
# 
# In this assignment you will perform the task of exploratory data analysis.
# You will find out the distribution of data, presence of outliers and also determine the correlation between different columns in the dataset.
# 

# ## Objectives
# 

# In this lab you will perform the following:
# 

# -   Identify the distribution of data in the dataset.
# 
# -   Identify outliers in the dataset.
# 
# -   Remove outliers from the dataset.
# 
# -   Identify correlation between features in the dataset.
# 

# * * *
# 

# ## Hands on Lab
# 

# Import the pandas module.
# 

# In[1]:


import pandas as pd


# Load the dataset into a dataframe.
# 

# In[2]:


df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv")


# ## Distribution
# 

# ### Determine how the data is distributed
# 

# The column `ConvertedComp` contains Salary converted to annual USD salaries using the exchange rate on 2019-02-01.
# 
# This assumes 12 working months and 50 working weeks.
# 

# Plot the distribution curve for the column `ConvertedComp`.
# 

# In[4]:


df
df['ConvertedComp'].plot(kind='kde')


# Plot the histogram for the column `ConvertedComp`.
# 

# In[5]:


df['ConvertedComp'].plot(kind='hist')


# What is the median of the column `ConvertedComp`?
# 

# In[6]:


df['ConvertedComp'].median()


# How many responders identified themselves only as a **Man**?
# 

# In[9]:


df['Gender'].value_counts()


# Find out the  median ConvertedComp of responders identified themselves only as a **Woman**?
# 

# In[19]:


w_df = df[df['Gender'] == 'Woman']
w_df['ConvertedComp'].median()


# Give the five number summary for the column `Age`?
# 

# **Double click here for hint**.
# 
# <!--
# min,q1,median,q3,max of a column are its five number summary.
# -->
# 

# In[21]:


df['Age'].describe()


# Plot a histogram of the column `Age`.
# 

# In[22]:


df['Age'].plot(kind='hist')


# ## Outliers
# 

# ### Finding outliers
# 

# Find out if outliers exist in the column `ConvertedComp` using a box plot?
# 

# In[23]:


df['ConvertedComp'].plot(kind='box')


# Find out the Inter Quartile Range for the column `ConvertedComp`.
# 

# In[25]:


q1 = df['ConvertedComp'].quantile(0.25)
q3 = df['ConvertedComp'].quantile(0.75)
iqr = q3 - q1
iqr


# Find out the upper and lower bounds.
# 

# In[26]:


print(q1)
print(q3)


# Identify how many outliers are there in the `ConvertedComp` column.
# 

# In[33]:


threshold = 1.5

outliers = df[(df['ConvertedComp'] < q1 - threshold * iqr) | (df['ConvertedComp'] > q3 + threshold * iqr)]
len(outliers)


# Create a new dataframe by removing the outliers from the `ConvertedComp` column.
# 

# In[47]:


df_no_outliers = df.drop(outliers.index)
df_no_outliers['ConvertedComp'].mean()


# ## Correlation
# 

# ### Finding correlation
# 

# Find the correlation between `Age` and all other numerical columns.
# 

# In[44]:


df.corr()['Age']


# ## Authors
# 

# Ramesh Sannareddy
# 

# ### Other Contributors
# 

# Rav Ahuja
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
# | ----------------- | ------- | ----------------- | ---------------------------------- |
# | 2020-10-17        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |
# 

#  Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2023-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 
