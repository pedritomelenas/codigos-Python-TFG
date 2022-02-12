#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


import time


# In[16]:


def PollardpB (n,x0,M):
    a=x0
    b=x0
    i=1
    d=1
    k=2
    while i<=M and d==1:
        if i>k:
            k=2*k
            b=a
        a=(a**2-1)%n
        d=math.gcd(a-b,n)
        i+=1
       
    if d!=1 and d!=n:
        return [d,int(n/d)]
    else:
        return 0


# In[31]:


inicio=time.time()
m=PollardpB(25769,2,12)
print(m)
fin=time.time()
print(fin-inicio)


# In[ ]:




