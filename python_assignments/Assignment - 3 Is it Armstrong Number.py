#!/usr/bin/env python
# coding: utf-8

# In[1]:


number = input("Please enter a number: ")
sum = 0
while not number.isdecimal():
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    number = input("Please enter a number: ")
if number.isdecimal():
    for i in range(len(number)):
         sum += int(number[i])**len(number)
    if  sum == int(number):
         print("{} is an Armstrong number".format(int(number)))
    else:
        print("{} is not an Armstrong number".format(int(number)))


# In[ ]:




