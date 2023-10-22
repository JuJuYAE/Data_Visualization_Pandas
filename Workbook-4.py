#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib as ply 


# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[16]:


df1 = pd.read_csv("df1",index_col = 0)


# In[17]:


df1.head()


# In[18]:


df2= pd.read_csv("df2")


# In[19]:


df2.head()


# In[22]:


df1["A"].hist()


# In[24]:


df1["A"].plot(kind = "hist", bins = 30)


# In[25]:


df2.head()


# In[28]:


df2.plot.area(alpha = 0.3)


# In[29]:


df2.plot.bar()


# In[32]:


df1["A"].plot.hist(bins = 30)


# In[47]:


df1.plot(kind = "line",y = "B", figsize = (12,3))


# In[54]:


df1.plot.scatter(x = "A", y = "B", s= df1["C"]*10)


# In[55]:


df = pd.DataFrame(np.random.randn(1000,2), columns = ["a", "b"])


# In[57]:


df.head(10)


# In[61]:


df.plot.hexbin(x = "a", y = "b", gridsize = 25, cmap = "coolwarm")


# In[64]:


df2["a"].plot.kde()


# In[ ]:




