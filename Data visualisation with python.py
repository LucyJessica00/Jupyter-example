#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from matplotlib import pyplot as plt


# In[8]:


x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]
plt.plot(x, y)
plt.plot(x, z)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["this is y", "this is z"])
plt.show()


# In[9]:


sample_data = pd.read_csv('sample_data.csv')


# In[10]:


sample_data


# In[11]:


type(sample_data)


# In[15]:


sample_data.column_c.iloc[0]


# In[18]:


plt.plot(sample_data.column_a, sample_data.column_b, 'o')
plt.plot(sample_data.column_a, sample_data.column_c)
plt.show()


# In[19]:


data = pd.read_csv('countries.csv')


# In[20]:


data


# In[21]:


# Compare the population growth in the US and China


# In[30]:


data[data.country == 'United States']


# In[27]:


us = data[data.country == 'United States']


# In[28]:


us 


# In[37]:


china = data[data.country == 'China']


# In[38]:


china


# In[41]:


plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population')
plt.show()


# In[42]:


us.population


# In[45]:


us.population / us.population.iloc[0] *100


# In[48]:


plt.plot(us.year, us.population / us.population.iloc[0] *100)
plt.plot(china.year, china.population / china.population.iloc[0] *100)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population growth (first year = 100)')
plt.show()


# In[ ]:




