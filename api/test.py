# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 10:50:08 2025

@author: user
"""
import time


text = "remind 5 丟垃圾"
text_strip = text.strip()     
parts = text.split(maxsplit=2)
time.sleep(int(parts[1]))
print (parts[1]) 

