#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy.plotting import plot
from sympy import *


# In[2]:


x = Symbol('x')
f = x**3 - 50*x
g = -x**4 + 88*x**2 - 241
i = f - g


# In[3]:


k = solve(i)
[[xelem.n().round(2),f.subs(x,xelem).n().round(2)]for xelem in k]


# In[4]:


plot(f,g)


# In[5]:


plot(f-g)


# In[ ]:




