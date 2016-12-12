#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:20:59 2016

@author: tomscott
"""

import matplotlib.pyplot as plt

# plt.show() to plot

import numpy as np
x = np.linspace(0,5,11)
y = x ** 2

# functional method (not generally used)

plt.plot(x,y)
plt.show()

plt.plot(x,y,'r-')  # add matlab style args

plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Title')
plt.show()

plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')

plt.show()

# object oriented method

fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X label')
axes.set_ylabel('Y label')
axes.set_title('Title')

axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes2.plot(y,x)
axes2.set_title('Small plot')

fig.show()

fig,axes = plt.subplots(nrows=1,ncols=2)  # create subplots
plt.tight_layout()  # remove overlapping

for current_ax in axes:  # iterate through axes
    current_ax.plot(x,y)
    
axes[0].set_title('First')
axes[1].set_title('Second')  # use indexes to call
axes[1].plot(y,x)

fig.show()

# figure size and DPI

fig = plt.figure(figsize=(3,2),dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)


fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()

fig.show()

# saving plots

fig.savefig('my_plot.png',dpi=200)  # specify extension and matplotlib will convert to that format

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2, label='X squared')
ax.plot(x,x**3, label='X cubed')
ax.legend(loc=0)  # 0 = best location as determined by matplotlib
fig.show()

# customising the graphs

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='#FF8C00',lw=2, alpha=0.75, ls='--', marker='o', markersize=5)  
fig.show()

# simple colour strings or hex codes
# ls = linestyle
# lw = linewidth
# marker






