#!/usr/bin/env python
# coding: utf-8

# In[27]:


import random
import time
print("This is a Dice Rolling Simulator.\n")
time.sleep(1)
dice_num=random.randint(1,6)
print(f"The number is {dice_num}.\n")
while True:
    ans=str(input("Do you want to roll the dice again?(yes/no)\n"))
    time.sleep(0.5)
    if ans=="yes":
        dice_num=random.randint(1,6)
        print(f"The number is {dice_num}.\n")
    else:
        break

