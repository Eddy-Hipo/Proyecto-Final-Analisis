#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlite3


# In[12]:


conn=sqlite3.connect("mars.db")
dfmars=pd.read_sql_query("SELECT * FROM AASSky_posts", conn)
dfmars=dfmars.set_index('index')
dfmars.to_csv('AASSky_posts.csv')

