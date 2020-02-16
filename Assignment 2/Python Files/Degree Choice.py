#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

firstgrad = pd.read_csv(r"~\Desktop\PDS-Assignment-1\Assignment 2\Raw Data\graduates-from-university-first-degree-courses-by-type-of-course.csv",
                       na_values = "na")
firstgrad = firstgrad[firstgrad.year >= 2000].reset_index(drop = True).set_index(["year", "type_of_course"])
firstgrad.no_of_graduates = firstgrad.no_of_graduates.fillna(0).astype(int)
firstgrad["total"] = firstgrad.no_of_graduates.groupby(level=["year", "type_of_course"]).sum()
firstgrad = firstgrad.reset_index()
firstgrad


# In[ ]:


sns.set(style="whitegrid")
sns.set(rc={'figure.figsize':(15.7,8.27)})

lineplot = sns.lineplot(x="year", y="total", hue = "type_of_course", marker = "o", data=firstgrad, palette="nipy_spectral")


plt.legend(loc='upper left')
lineplot.set(xlabel='Year', ylabel='Graduates', title="Number Of Graduates In Different Faculties Over The Years")
plt.show(lineplot)

