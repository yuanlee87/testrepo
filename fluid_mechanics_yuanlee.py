#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 01:20:16 2020

@author: yuanlee
"""


v=float(input('Enter the volicity of water in the pipe: '))
d=float(input("Enter the pipe's diameter: "))
t=float(input('Enter the temperature in °C as 5, 10 or 15: '))
if t==5:
    print('The Reynolds number for flow at',v, 'm/s in a', d, 'm diameter pipe at',
          t,'°c is',format(v*d/(1.49*10**-6), '.2e'), end='.')
elif t==10:
     print('The Reynolds number for flow at',v, 'm/s in a', d, 'm diameter pipe at',
          t,'°c is',format(v*d/(1.31*10**-6), '.2e'), end='.')
else:
     print('The Reynolds number for flow at',v, 'm/s in a', d, 'm diameter pipe at',
          t,'°c is',format(v*d/(1.15*10**-6), '.2e'), end='.')
     