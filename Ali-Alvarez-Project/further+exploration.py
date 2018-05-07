
# coding: utf-8

# In[12]:

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency


# In[45]:

def load_data():   
    df = pd.DataFrame([ 
        ['Amphibian',7,72,0.911392],
        ['Bird',75,	413,0.846311],
        ['Fish',11,	115,0.912698],
        ['Mammal',30,146,0.829545],
        ['Nonvascular Plant',5,328,0.984985],
        ['Reptile',	5,73,0.935897],
        ['Vascular Plant',46,4216,0.989207] ],
        columns=['category','not_protected','protected','percent_protected'])
    return df


# In[46]:

def chi(cat1, cat2,contingency):
    chi2, pval, dof, expected = chi2_contingency(contingency)
    if pval<0.05: 
        print("significant difference exists between", cat1," and ", cat2) 


# In[47]:

#_main_chi_study
df=load_data()
for row in range (0,len(df)-1):
    cat1=df.loc[row][0]
    for row2 in range(1,len(df)):
        cat2=df.loc[row2][0]
        # calculating contingency
        contingency = [df.loc[row][1],df.loc[row][2]],[df.loc[row+1][1],df.loc[row+1][2]]
        chi(cat1,cat2,contingency)


# In[ ]:



