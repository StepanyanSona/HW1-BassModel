#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def bass_model(t, p, q, M):
    return (M * (p + q) ** 2 * np.exp(-(p + q) * t)) / (p + q * np.exp(-(p + q) * t)) ** 2

