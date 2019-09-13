#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
str = '21/01/2017'
date_format ="%d/%m/%y" #?
datetime_value = time.strptime(str,date_format)
print(datetime_value)


# In[6]:


import pandas as pd
df = pd.DataFrame({'Click_Id':['A','B','C','D','E'],'Count':[100,200,300,400,250]})
df.rename(columns = {'Count':'Click_Count'})
print(df.columns)
#Question4


# In[17]:


A = {'india', 'pakistan', 'australia', 'newzealand', 'india', 'kiwis'}
B = {'england', 'westIndies','sriLanka','afghanistan', 'pakistan'}
print(A - B)
print(B&A)
print(A.union(B))
print(B|A)
print(B - A)


# In[ ]:




