#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
import sqlite3


# In[2]:


def find_2nd(string, substring):
    return string.find(substring, string.find(substring)+1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))


# In[3]:


response = requests.get("https://skyandtelescope.org/?s=mars")
soup=BeautifulSoup(response.content, "lxml")

Category=[]
post_category= soup.find_all("a", class_="c-cat-link")
for element in post_category:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Category.append(limpio.strip())

New=[]
post_new= soup.find_all("p", class_= "media-block__excerpt brief")
for element in post_new:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    New.append(limpio.strip())

Author=[]
post_author= soup.find_all("a", class_="author")
for element in post_author:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Author.append(limpio.strip())

Date=[]
post_date= soup.find_all("span", class_="date")
for element in post_date:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Date.append(limpio.strip())
# ____________________________________________________________________________

response = requests.get("https://skyandtelescope.org/page/2/?s=mars")
soup=BeautifulSoup(response.content, "lxml")

post_category= soup.find_all("a", class_="c-cat-link")
for element in post_category:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Category.append(limpio.strip())

post_new= soup.find_all("p", class_= "media-block__excerpt brief")
for element in post_new:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    New.append(limpio.strip())

post_author= soup.find_all("a", class_="author")
for element in post_author:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Author.append(limpio.strip())

post_date= soup.find_all("span", class_="date")
for element in post_date:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Date.append(limpio.strip())
# ____________________________________________________________________________

response = requests.get("https://skyandtelescope.org/page/3/?s=mars")
soup=BeautifulSoup(response.content, "lxml")

post_category= soup.find_all("a", class_="c-cat-link")
for element in post_category:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Category.append(limpio.strip())

post_new= soup.find_all("p", class_= "media-block__excerpt brief")
for element in post_new:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    New.append(limpio.strip())

post_author= soup.find_all("a", class_="author")
for element in post_author:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Author.append(limpio.strip())

post_date= soup.find_all("span", class_="date")
for element in post_date:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Date.append(limpio.strip())
# ____________________________________________________________________________

response = requests.get("https://skyandtelescope.org/page/4/?s=mars")
soup=BeautifulSoup(response.content, "lxml")

post_category= soup.find_all("a", class_="c-cat-link")
for element in post_category:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Category.append(limpio.strip())

post_new= soup.find_all("p", class_= "media-block__excerpt brief")
for element in post_new:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    New.append(limpio.strip())

post_author= soup.find_all("a", class_="author")
for element in post_author:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Author.append(limpio.strip())

post_date= soup.find_all("span", class_="date")
for element in post_date:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Date.append(limpio.strip())
# ____________________________________________________________________________    

response = requests.get("https://skyandtelescope.org/page/5/?s=mars")
soup=BeautifulSoup(response.content, "lxml")

post_category= soup.find_all("a", class_="c-cat-link")
for element in post_category:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Category.append(limpio.strip())

post_new= soup.find_all("p", class_= "media-block__excerpt brief")
for element in post_new:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    New.append(limpio.strip())

post_author= soup.find_all("a", class_="author")
for element in post_author:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Author.append(limpio.strip())

post_date= soup.find_all("span", class_="date")
for element in post_date:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Date.append(limpio.strip())

data= {'Category': Category, 'New': New, 'Author': Author, 'Date': Date}
mars= pd.DataFrame(data)


# In[4]:


conn= sqlite3.connect("mars.db")
mars.to_sql("AASSky_posts", conn, if_exists='replace')
conn.close()

