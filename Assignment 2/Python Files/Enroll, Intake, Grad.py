#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

merged = pd.read_csv(r"~\Desktop\PDS-Assignment-1\Assignment 2\After Cleansing\Merged.csv")
merged = merged[merged.year >= 2000]
# merged


# In[ ]:


NUS = merged[["year", "sex","nus", "total", "type"]]
NUS


# In[ ]:


sns.set(style="whitegrid")
sns.set(rc={'figure.figsize':(15.7,8.27)})
barplot = sns.barplot(x="year", y="nus", hue= "type", data=NUS, palette="GnBu_d", ci=None)


barplot.set(xlabel='Year', ylabel='Total Number Of Students In NUS', title="Enrollment vs Inrolement vs Graduates")
plt.legend(loc='upper left')
plt.show(barplot)


# In[ ]:


intake_grad = NUS[NUS.type !="enroll"]
intake_grad = intake_grad[intake_grad.sex != "MF"].sort_values("year").reset_index(drop = True)
intake_grad


# In[ ]:


import plotly.express as px
fig = px.box(intake_grad, x="type", y="total", color="sex",
             notched = True, # used notched shape
             title="Boxplot of Intake and Graduate Of Different Genders In Total Over The Years",
             hover_data = ["year"],
             points = "all")
fig.show()


# In[ ]:


medians = intake_grad.groupby(['type',"sex"])["total"].median()
print(medians)

