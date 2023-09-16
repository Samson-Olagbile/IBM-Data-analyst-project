#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2023-01-01">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Data Visualization Lab**
# 

# Estimated time needed: **45 to 60** minutes
# 

# In this assignment you will be focusing on the visualization of data.
# 
# The data set will be presented to you in the form of a RDBMS.
# 
# You will have to use SQL queries to extract the data.
# 

# ## Objectives
# 

# In this lab you will perform the following:
# 

# -   Visualize the distribution of data.
# 
# -   Visualize the relationship between two features.
# 
# -   Visualize composition of data.
# 
# -   Visualize comparison of data.
# 

# <hr>
# 

# ## Demo: How to work with database
# 

# Download database file.
# 

# In[8]:


get_ipython().system('pip install wget')

import wget

file = wget.download('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m4_survey_data.sqlite')


# Connect to the database.
# 

# In[66]:


import sqlite3
conn = sqlite3.connect(file) # open a database connection


# Import pandas module.
# 

# In[67]:


import pandas as pd


# ## Demo: How to run an sql query
# 

# In[17]:


# print how many rows are there in the table named 'master'
QUERY = """
SELECT COUNT(*)
FROM master
"""

# the read_sql_query runs the sql query and returns the data as a dataframe
df = pd.read_sql_query(QUERY,conn)
df.head()


# ## Demo: How to list all tables
# 

# In[68]:


# print all the tables names in the database
QUERY = """
SELECT name as Table_Name FROM
sqlite_master WHERE
type = 'table'
"""
# the read_sql_query runs the sql query and returns the data as a dataframe
pd.read_sql_query(QUERY,conn)


# ## Demo: How to run a group by query
# 

# In[19]:


QUERY = """
SELECT Age,COUNT(*) as count
FROM master
group by age
order by age
"""
pd.read_sql_query(QUERY,conn)


# ## Demo: How to describe a table
# 

# In[20]:


table_name = 'master'  # the table you wish to describe

QUERY = """
SELECT sql FROM sqlite_master
WHERE name= '{}'
""".format(table_name)

df = pd.read_sql_query(QUERY,conn)
print(df.iat[0,0])


# # Hands-on Lab
# 

# ## Visualizing distribution of data
# 

# ### Histograms
# 

# Plot a histogram of `ConvertedComp.`
# 

# In[23]:


QUERY = """
SELECT ConvertedComp
FROM master

"""
df = pd.read_sql_query(QUERY,conn)
df.plot(kind='hist')


# ### Box Plots
# 

# Plot a box plot of `Age.`
# 

# In[24]:


QUERY = """
SELECT Age
FROM master
"""
df = pd.read_sql_query(QUERY,conn)
df.plot(kind='box')


# ## Visualizing relationships in data
# 

# ### Scatter Plots
# 

# Create a scatter plot of `Age` and `WorkWeekHrs.`
# 

# In[26]:


QUERY = """
SELECT Age, WorkWeekHrs
FROM master

"""
df = pd.read_sql_query(QUERY,conn)
df.plot(kind='scatter', x='Age', y= 'WorkWeekHrs')


# ### Bubble Plots
# 

# Create a bubble plot of `WorkWeekHrs` and `CodeRevHrs`, use `Age` column as bubble size.
# 

# In[30]:


QUERY = """
SELECT Age, WorkWeekHrs, CodeRevHrs
FROM master

"""
df = pd.read_sql_query(QUERY,conn)
df.plot(kind='scatter', x='WorkWeekHrs', y= 'CodeRevHrs', s=df['Age'])


# ## Visualizing composition of data
# 

# ### Pie Charts
# 

# Create a pie chart of the top 5 databases that respondents wish to learn next year. Label the pie chart with database names. Display percentages of each database on the pie chart.
# 

# In[72]:


QUERY = """

select count(LanguageDesireNextYear) as Count,LanguageDesireNextYear 
from LanguageDesireNextYear 
group by LanguageDesireNextYear 
order by count(LanguageDesireNextYear) DESC 
LIMIT 5


"""

df2=pd.read_sql_query(QUERY,conn)
df2


# In[75]:


QUERY = """

select count(LanguageWorkedWith) as Count,LanguageWorkedWith 
from LanguageWorkedWith 
group by LanguageWorkedWith 
order by count(LanguageWorkedWith) DESC 

"""

df2=pd.read_sql_query(QUERY,conn)
df2


# In[81]:


QUERY = """
select count(DatabaseWorkedWith), DatabaseWorkedWith
from DatabaseWorkedWith
group by DatabaseWorkedWith 
order by count(DatabaseWorkedWith) DESC 
LIMIT 5
"""

df2=pd.read_sql_query(QUERY,conn)
df2


# In[38]:


QUERY = """

select count(DatabaseDesireNextYear) as Count,DatabaseDesireNextYear 
from DatabaseDesireNextYear 
group by DatabaseDesireNextYear 
order by count(DatabaseDesireNextYear) DESC 
LIMIT 5

"""

df2=pd.read_sql_query(QUERY,conn)

df2.set_index('DatabaseDesireNextYear',inplace=True)

df2.plot(kind='pie', y='Count', title="Title", legend=False,                    autopct='%1.1f%%')


# ### Stacked Charts
# 

# Create a stacked chart of median `WorkWeekHrs` and `CodeRevHrs` for the age group 30 to 35.
# 

# In[47]:


QUERY = """
SELECT Age, WorkWeekHrs, CodeRevHrs
FROM master
WHERE Age BETWEEN 30 AND 35
"""
df = pd.read_sql_query(QUERY,conn)
df1 = df.groupby('Age').median()
df1.plot(kind='bar', stacked=True)


# ## Visualizing comparison of data
# 

# ### Line Chart
# 

# Plot the median `ConvertedComp` for all ages from 45 to 60.
# 

# In[48]:


QUERY = """
SELECT Age, ConvertedComp
FROM master
WHERE Age BETWEEN 45 AND 60

"""
df = pd.read_sql_query(QUERY,conn)
df1 = df.groupby('Age').median()
df1.plot(kind='line')


# ### Bar Chart
# 

# Create a horizontal bar chart using column `MainBranch.`
# 

# In[63]:


QUERY = """
SELECT MainBranch, COUNT(MainBranch) AS Count_of_mainBranch
FROM master
GROUP BY MainBranch
"""
df = pd.read_sql_query(QUERY,conn,)
df.set_index('MainBranch', inplace=True)
df.plot(kind='barh',)


# In[83]:


QUERY = """
SELECT DevType, count(DevType)
FROM DevType
group by DevType 
order by count(DevType) DESC 
"""
df = pd.read_sql_query(QUERY,conn)
df


# Close the database connection.
# 

# In[64]:


conn.close()


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
