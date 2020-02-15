#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

employment = pd.read_csv(r"~\Desktop\School Related\PDS-Assignment-1\Assignment 2\Raw Data\graduate-employment-survey-ntu-nus-sit-smu-sutd.csv", 
                         na_values = "na").fillna(0)
employment = employment[employment.university == "National University of Singapore"]
employment = employment[employment.school.isin(["Faculty of Arts & Social Sciences", "Faculty of Engineering", "Faculty of Science"])]
employment


# In[ ]:


#In accordance to top 3 courses intake in NUS, the graduation will be from these faculties
#Engineering Sciences, Humanities & Social Sciences, Natural, Physical & Mathematical Sciences
sns.set(style="whitegrid")
sns.set(rc={'figure.figsize':(15.7,8.27)})


scatterplot = sns.scatterplot(x=employment.employment_rate_ft_perm , 
                              y=employment.gross_monthly_mean, 
                              hue=employment.school, 
                              style = employment.school,
                              data=employment)


scatterplot.set_ylim([2000, 4500])
scatterplot.set_xlim([45, 100])
scatterplot.set(xlabel='Employment Rate(Full Time)',
                ylabel='Gross Monthly Mean Salary', 
                title="Trend Of Employment Rate Against Gross Monthly Mean Salary")
plt.show(scatterplot)

