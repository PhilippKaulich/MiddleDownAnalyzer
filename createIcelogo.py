# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:27:42 2023

@author: Philipp
"""


import logomaker as lm

import pandas as pd


data = pd.read_csv("E:\\ice.csv")

print(data)
logo = lm.Logo(df=data,
               font_name='Arial Rounded MT Bold',
               fade_below=0.5,
               shade_below=0.5,
               stack_order='small_on_top',
               figsize=(10,3))

# set axes labels
logo.ax.set_xlabel('Position',fontsize=14)
logo.ax.set_ylabel("$-\Delta \Delta G$ (kcal/mol)", labelpad=-1,fontsize=14)