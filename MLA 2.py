#!/usr/bin/env python
# coding: utf-8

# # Python Assignment 2 S.Y. D. S

# # Basic Exercises on Data Importing - Understanding - Manipulating - Analysis - Visualization

# # Section-1: The pupose of the below exercises (1-7) is to create dictionary and convert into dataframes, how to diplay etc...

# # The below exercises required to create data

# # 1. Import the necessary libraries (pandas, numpy, datetime, re etc)

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
import re

# set the graphs to show in the jupyter notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# set seabor graphs to a better style
sns.set(style="ticks")


# 2. Run the below line of code to create a dictionary and this will be used for below exercises¶

# In[5]:


raw_data = {"name": ['Bulbasaur', 'Charmander','Squirtle','Caterpie'],
            "evolution": ['Ivysaur','Charmeleon','Wartortle','Metapod'],
            "type": ['grass', 'fire', 'water', 'bug'],
            "hp": [45, 39, 44, 45],
            "pokedex": ['yes', 'no','yes','no']        
            }


# In[6]:


pokemon= pd.DataFrame(raw_data)
pokemon


# 3. Assign it to a object called pokemon and it should be a pandas DataFrame

# In[7]:


pokemon= pd.DataFrame(raw_data)
pokemon


# 4. If the DataFrame columns are in alphabetical order, change the order of the columns as name, type, hp, evolution, pokedex

# In[8]:


pokemon=pokemon[['name','type','hp','evolution','pokedex']]
pokemon


# 5. Add another column called place, and insert places (lakes, parks, hills, forest etc) of your choice.

# In[9]:


pokemon['place']= ['lakes', 'parks', 'hills', 'forest']
pokemon


# 6. Display the data type of each column

# In[10]:


pokemon.dtypes


# 7. Display the info of dataframe

# In[11]:


pokemon.info()


# # Section-2
# 
# ## The below exercises required to use wine.data

# 8. Import the dataset wine.txt from the folder and assign it to a object called wine
# Please note that the original data text file doesn't contain any header. Please ensure that when you import the data, you should use a suitable argument so as to avoid data getting imported as header.

# In[13]:


wine=pd.read_csv("wine.csv")
wine.head()


# 9. Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns

# In[15]:


wine.drop(columns=["Wine","Ash","Acl","Phenols","Nonflavanoid.phenols","Color.int","OD"],inplace=True)
wine

### 10. Assign the columns as below:

The attributes are (dontated by Riccardo Leardi, riclea '@' anchem.unige.it):  
1) alcohol  
2) malic_acid  
3) alcalinity_of_ash  
4) magnesium  
5) flavanoids  
6) proanthocyanins  
7) hue 
# In[16]:


wine.columns=['alcohol', 'malic_acid','alcalinity_of_ash','magnesium','flavanoids','proanthocyanins', 'hue']
wine


# 11. Set the values of the first 3 values from alcohol column as NaN

# In[18]:


import numpy as np
wine.alcohol.iloc[0:3] =np.nan
wine


# 12. Now set the value of the rows 3 and 4 of magnesium as NaN

# In[19]:


wine.magnesium.iloc[2:4]=np.nan
wine


# 13. Fill the value of NaN with the number 10 in alcohol and 100 in magnesium¶

# In[20]:


wine.alcohol=wine.alcohol.fillna(10)
wine.magnesium=wine.magnesium.fillna(100)
wine


# 14. Count the number of missing values in all columns.
# ​

# In[21]:


wine.isna().sum()


# 15. Create an array of 10 random numbers up until 10 and save it.
# ​

# In[22]:


Q15=np.random.randint(0,11,10)
Q15


# 16. Set the rows corresponding to the random numbers to NaN in the column alcohol

# In[23]:


wine.alcohol.iloc[Q15]=np.nan
wine.head(20)


# ### 17.  How many missing values do we have now?

# In[24]:


wine.isna().sum()


# 18. Print only the non-null values in alcohol

# In[25]:


wine[['alcohol']].dropna()


# 19. Delete the rows that contain missing values

# In[26]:


wine=wine.dropna()
wine


# 20. Reset the index, so it starts with 0 again

# In[27]:


wine.reset_index(drop=True)


# In[ ]:




