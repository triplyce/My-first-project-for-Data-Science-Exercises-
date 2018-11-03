
# coding: utf-8

# # Numpy

# In[1]:


import numpy as np


# In[2]:


a=np.array([1,2,3,4])
a


# In[6]:


a=np.array([(1,2,3,4),(5,6,7,8)])
a


# ## Aprendendo2

# In[13]:


a=np.array([(1,2,3,4),(5,6,7,8)])
a.ndim


# In[14]:


a=np.array([(1,2,3,4),(5,6,7,8)])
a.itemsize


# In[15]:


a=np.array([(1,2,3,4),(5,6,7,8)])
a.dtype


# In[16]:


a=np.array([(1,2,3,4),(5,6,7,8)])
a.shape


# In[21]:


a=np.array([(1,2,3,4),(5,6,7,8)])
a.reshape(4,2)


# In[22]:


a=np.array([(1,2,3,4),(5,6,7,8)])
a[0,2]


# In[23]:


a=np.array([(1,2,3,4),(5,6,7,8)])
a[0:,3]


# In[24]:


a=np.linspace(1,4,20)
a


# In[26]:


a=np.linspace(1,4,6)
a.min()
a.max()
a.sum()


# In[28]:


a=np.array([(1,2,3,4),(5,6,7,8)])
a.sum(axis=0)


# In[29]:


a=np.array([(1,2,3,4),(5,6,7,8)])
np.sqrt(a)


# In[30]:


x=np.array([(1,2,3,4),(5,6,7,8)])
y=np.array([(1,2,3,4),(5,6,7,8)])
x/y


# ### Vertical

# In[35]:


x=np.array([(1,2,3,4),(5,6,7,8)])
y=np.array([(1,2,3,4),(5,6,7,8)])
np.hstack ((x,y))

