#!/usr/bin/env python
# coding: utf-8

# In[47]:


# Task 1, Question 1

print ("Hello World")


# In[28]:


# Task 1, Question 2

for i in range(2000, 3200):
    if i % 7 == 0 and i % 5 != 0:
        print(i,", ", end="")


# In[31]:


# Task 1, Question 3 

F = input ("Enter your First Name: ")
L = input ("Enter your Last Name: ")
print(L,F)


# In[49]:


# Task 1, Question 4

import math
P = math.pi
r = 12/2
v=(4/3)*P*r**3
print(v)


# In[110]:


# Task 2, Question 1

a = list(input('Enter list of numbers seperated by ",": ' ))
l=[]
for i in range(0, len(a)):
    if a[i] != "," :
        l.append(int(a[i]))
print(l)


# In[4]:


# Task 2, Question 2
n=5
for i in range(n, -n,-1):
	for j in range(n-abs(i)):
		print("*", end="")
	print()


# In[5]:


# Task 2, Question 2 without nested for loop
n=5
for i in range(n, -n,-1):
	print((n-abs(i))*"*")


# In[3]:


# Task 2, Question 3

i=input('enter a word: ')
for j in range(len(i),0,-1):
	print(i[j-1], end='')


# In[7]:


# Task 2, Question 4

print("WE, THE PEOPLE OF INDIA, \n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST SECULAR, DEMOCRATIC REPUBLIC \n\t\tand to secure to all its citizens")

