#!/usr/bin/env python
# coding: utf-8

# In[11]:


#lab number 6
import numpy as np

# rule number 1

c = float(input("input c"))

da = float(input("error in a"))

def rule1 (c,da):
    dT = (c*da)
    return (dT)

dT = rule1(c,da)

print("Total error =", dT)




# In[15]:


#rule 2

m = float(input("input your exponent: "))
a = float(input("Base of exponent or a: "))
da = float(input("Error in base of exponent or error in a: "))
c = float(input("constant we are multiplying a by: "))

def rule2 (m,a,da,c):
    dT = c*(m*(a**(m-1)))*da
    return dT
dT = rule2(m,a,da,c)

print("Total error =", dT)


# In[16]:


#rule 4
print("constants are irlevient")

a = float(input("value in base A: "))
da = float(input("error in A: "))
m = float(input("The power A is being raised: "))

b = float(input("value for base B: "))
db = float(input("error in B: "))
n = float(input("the power B is being raised: "))

q = float(input("The final value aka Q: "))

def rule4(a,da,m,b,db,n):
    dT = (((m*da)/a)**2+((n*db)/b)**2)
    return dT
dT = rule4(a,da,m,b,db,n)

print("Total error =", dT)


# In[29]:


# rule 3

da = float(input("error in A: "))
db = float(input("error in B: "))

def rule4(da,db):
    dT = ((da**2)+(db**2))**(1/2)
    return dT
dT = rule4(da,db)

print(dT)


# In[ ]:





# In[ ]:




