#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

overseas = pd.read_csv(r"~\Desktop\School Related\PDS-Assignment-1\Assignment 2\After Cleansing\overseas_data.csv")
overseas


# In[ ]:


labels = overseas.Field.unique()
sg = overseas[overseas.Country == "Singapore"]
overseas = overseas[overseas.Country == "Outside Singapore- Total"]


# In[ ]:


import plotly.graph_objects as go
from plotly.subplots import make_subplots


fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels=labels, values=sg["Graduates (Thousands)"], name="Singapore"),
              1, 1)
fig.add_trace(go.Pie(labels=labels, values=overseas["Graduates (Thousands)"], name="Abroad"),
              1, 2)


fig.update_traces(hole=.4, hoverinfo="label+percent+name")

fig.update_layout(
    title_text="Singapore vs Abroad",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='Singapore', x=0.15, y=0.5, font_size=15, showarrow=False),
                 dict(text='Abroad', x=0.83, y=0.5, font_size=15, showarrow=False)])
fig.show()

