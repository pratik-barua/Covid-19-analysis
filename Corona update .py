#!/usr/bin/env python
# coding: utf-8

# # Corona Virus Update in Bangladesh

# In[1]:


#importing panda
import pandas as pd


# In[2]:


#file path
path="C:\\Users\\user\\Desktop\\Projects\\Corona update analysis\\corona update.csv"
#importin csv file
df=pd.read_csv(path)
#printing csv file
df.head()


# In[21]:



import matplotlib as plt
from matplotlib import pyplot
import numpy as np
pyplot.style.use('ggplot')
count,bin_edges=np.histogram(df['New_cases'])

df['New_cases'].plot(kind='hist',figsize=(8,6),xticks=bin_edges)

# set x/y labels and plot title
pyplot.xlabel("New_cases")
pyplot.ylabel("count")
pyplot.title("Histogram of New Cases")
pyplot.show()


# In[22]:


import matplotlib as plt
from matplotlib import pyplot
count,bin_edges=np.histogram(df['Death'])

df['Death'].plot(kind='hist',figsize=(8,6),xticks=bin_edges)

# set x/y labels and plot title
plt.pyplot.xlabel("Death")
plt.pyplot.ylabel("count")
plt.pyplot.title("Histogram of Death")


# In[29]:


#New cases found according to boolian function
df.set_index('Date',inplace=True)
NewCasesFound=df['New_cases']!=0
print("New cases found to boolian function")
print(NewCasesFound)


# In[7]:


#Death occured according to boolian function
DeathFound=df['Death']!=0
print('Death occured according to boolian function')
print(DeathFound)


# In[8]:


plt.style.use(['ggplot'])


# In[24]:


#Plot of new cases each day
df["New_cases"].plot(kind='line',figsize=(8,6))
pyplot.title('Plot of New Cases per day')
pyplot.ylabel("Number of New Case")
pyplot.show()


# In[25]:



#Plot of death each day
df["Death"].plot(kind="line",figsize=(8,6))
pyplot.title('Plot of Death per day')
pyplot.ylabel("Number of Death")
pyplot.show()


# In[30]:



#Bar chart of new cases each day
df["New_cases"].plot(kind="bar",figsize=(14,10))
pyplot.title('Bar chart of New Cases per day')
pyplot.ylabel("Number of New Case")

pyplot.annotate('',                      # s: str. Will leave it blank for no text
             xy=(33, 492),             # place head of the arrow at point (year 2012 , pop 70)
             xytext=(20,80),         # place base of the arrow at point (year 2008 , pop 20)
             xycoords='data',         # will use the coordinate system of the object being annotated 
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
            )
pyplot.annotate('From 5th April New cases started to increase', # text to display
             xy=(22, 180),                    # start the text at at point (year 2008 , pop 30)
             rotation=57.3,                  # based on trial and error to match the arrow
             va='bottom',                    # want the text to be vertically 'bottom' aligned
             ha='left',                      # want the text to be horizontally 'left' algned.
            )

pyplot.show()


# In[31]:


#Bar chart of death each day
df["Death"].plot(kind="bar",figsize=(14,10))
pyplot.title('Bar chart of Death per day')
pyplot.ylabel("Number of Death")
pyplot.show()


# In[13]:


path="C:\\Users\\user\\Desktop\\Projects\\Corona update analysis\\corona update.csv"
#importin csv file
df=pd.read_csv(path)


# In[14]:


df['New_cases'].plot(kind='box', figsize=(10, 10))

pyplot.title('Box plot of New Cases')
pyplot.ylabel('Number of New Cases')

pyplot.show()


# In[15]:


df['Death'].plot(kind='box', figsize=(10, 10))

pyplot.title('Box plot of Death')
pyplot.ylabel('Number of Death')

pyplot.show()


# In[16]:


df.plot(kind='scatter', x='Date', y='New_cases', figsize=(25, 8), color='darkblue')

pyplot.title('Scatter Plot of New Cases')
pyplot.xlabel('Day')
pyplot.ylabel('Number of New Cases')

pyplot.show()


# In[17]:


df.plot(kind='scatter', x='Date', y='Death', figsize=(25, 8), color='darkblue')

pyplot.title('Scatter Plot of Death')
pyplot.xlabel('Day')
pyplot.ylabel('Number of Death')

pyplot.show()


# In[19]:



# normalize Brazil data
norm_newcase= (df['New_cases'] - df['New_cases'].min()) / (df['New_cases'].max() - df['New_cases'].min())

# normalize Argentina data
norm_death = (df['Death'] - df['Death'].min()) / (df['Death'].max() - df['Death'].min())
ax0 = df.plot(kind='scatter',
                    x='Date',
                    y='New_cases',
                    figsize=(27, 12),
                    alpha=0.5,                  # transparency
                    color='green',
                    s=norm_newcase * 2000 + 10,  # pass in weights 
                   
                   )

# Argentina
ax1 = df.plot(kind='scatter',
                    x='Date',
                    y='Death',
                    alpha=0.5,
                    color="blue",
                    s=norm_death * 2000 + 10,
                    ax = ax0
                   )

ax0.set_ylabel('Number of New Cases and Deaths')
ax0.set_title('New Cases and Deaths from 16th March')
ax0.legend(['New Cases', 'Deaths'], loc='upper left', fontsize='x-large')


# In[ ]:




