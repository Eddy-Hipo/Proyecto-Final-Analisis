#!/usr/bin/env python
# coding: utf-8

# In[1]:


from facebook_scraper import get_posts
import pandas as pd
import sqlite3


# In[2]:


Link=[]
Text=[]
Likes=[]
Comments=[]
Shares=[]
for post in get_posts('NASA',pages=78): 
    if ('Mars' in post['text']):
        Link.append(post['post_url'])
        Text.append(post['text'])
        Likes.append(post['likes'])
        Comments.append(post['comments'])
        Shares.append(post['shares'])
        
data= {'Link': Link, 'Text': Text, 'Likes': Likes, 'Comments': Comments, 'Shares': Shares}
mars= pd.DataFrame(data)


# In[3]:


conn= sqlite3.connect("mars.db")
mars.to_sql("NASA_posts", conn, if_exists='replace')
conn.close()

