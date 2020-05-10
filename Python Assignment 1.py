#!/usr/bin/env python
# coding: utf-8

# In[47]:


# Task 1, Question 1
# Install Jupyter notebook and run the first program and share the screenshot of the output.

print ("Hello World")


# In[28]:


# Task 1, Question 2
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

for i in range(2000, 3200):
    if i % 7 == 0 and i % 5 != 0:
        print(i,", ", end="")


# In[31]:


# Task 1, Question 3 
# Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.

F = input ("Enter your First Name: ")
L = input ("Enter your Last Name: ")
print(L,F)


# In[49]:


# Task 1, Question 4
# Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r 3

import math
P = math.pi
r = 12/2
v=(4/3)*P*r**3
print(v)


# In[8]:


# Task 2, Question 1
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list.

a = list(input('Enter list of numbers seperated by ",": ' ))
l=[]
for i in range(0, len(a)):
    if a[i] != "," :
        l.append(int(a[i]))
print(l)


# In[4]:


# Task 2, Question 2
# Create the below pattern using nested for loop in Python.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

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
# Write a Python program to reverse a word after accepting the input from the user.

i=input('enter a word: ')
for j in range(len(i),0,-1):
	print(i[j-1], end='')


# In[7]:


# Task 2, Question 4
# Write a Python Program to print the given string in the format specified in the sample output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens
# Sample Output:
# WE, THE PEOPLE OF INDIA,
#     having solemnly resolved to constitute India into a SOVEREIGN, !
#         SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
#         and to secure to all its citizens

print("WE, THE PEOPLE OF INDIA, \n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST SECULAR, DEMOCRATIC REPUBLIC \n\t\tand to secure to all its citizens")

