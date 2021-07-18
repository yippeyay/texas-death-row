#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[2]:


response=requests.get("https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html")
doc=BeautifulSoup(response.text, 'html.parser')


# In[3]:


txtable=doc.find('table')
txtable


# In[4]:


all_inmates=txtable.find_all('tr')
final_list=pd.DataFrame()
for inmate in all_inmates[1:]:
    #print(inmate)
    inmate_data= inmate.find_all('td')
    execution=inmate_data[0].text
    base_url="https://www.tdcj.texas.gov/death_row/"
    url=base_url+inmate_data[1].find('a')['href']
    statement=base_url+inmate_data[2].find('a')['href']
    last_name=inmate_data[3].text
    first_name=inmate_data[4].text
    #skipped 5 on purpose
    age=inmate_data[6].text
    execution_date=inmate_data[7].text
    race=inmate_data[8].text
    county=inmate_data[9].text
    dict={} 
    dict['number']=execution
    dict['url']=url
    dict['last_statement']=statement
    dict['last_name']=last_name
    dict['first_name']=first_name
    dict['age']=age
    dict['execution_date']=execution_date
    dict['race']=race
    dict['county']=county
    final_list=final_list.append(dict,ignore_index=True)


# In[5]:


final_list


# In[6]:


df=final_list


# In[98]:


pd.to_datetime(execution_date)


# In[100]:


df['age'] = df['age'].astype(int)
df['number'] = df['number'].astype(int)


# In[7]:


df=final_list


# In[ ]:


df.to_csv("tx-executions.csv")

