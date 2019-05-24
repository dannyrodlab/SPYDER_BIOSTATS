# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:09:44 2019

@author: BATMAN
"""
## Set folders
import os
PATH_INPUT = os.path.abspath("./input/")
if not(os.path.exists(PATH_INPUT)): os.mkdir('input')
assert os.path.exists(PATH_INPUT), "Oh no! Input folder is missing :("
PATH_FIGURES = os.path.abspath("./figures/")
if not(os.path.exists(PATH_FIGURES)): os.mkdir('figures')
assert os.path.exists(PATH_FIGURES), "Oh no! Figures folder is missing :("
## Data type
EXT_DATA = '.xlsx'
EXT_FIG = '.png'
## Read data
PATH_DATA = os.path.join(PATH_INPUT, '20190523_BIOSTATS_PROJECT_Data_Columns'+ EXT_DATA)
assert os.path.exists(PATH_DATA), "Oh no! Data is missing :("

## Figure parameters
figures_size = (8,8)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
import datetime

df = pd.read_excel(PATH_DATA)
print(df.head())
list(df)
# %% 
## Read variables
#[rows, colums] = df.shape

## Get current time
now = datetime.datetime.now()
NAME_TIME = now.strftime("%Y%m%d-%H%M")

plt.figure(1)
plt.plot(df.count().sort_values(),'bo')
plt.xticks(rotation=45)
plt.ylabel('Numero de datos')
plt.tight_layout()
## Name your child
NAME_FIGURE_1 = 'DATA_SIZES'
PATH_FIGURE_1 = os.path.join(PATH_FIGURES, NAME_TIME + '_' + NAME_FIGURE_1 + EXT_FIG)
plt.savefig( PATH_FIGURE_1 , dpi=100 )

plt.figure(2)
meds = df.median()
meds = meds.sort_values()
boxplot = df[meds.index].boxplot(rot=45,fontsize=12)
plt.ylabel('Tiempo de juego [segundos]')
plt.tight_layout()
## Name your child
NAME_FIGURE_2 = 'BOXPLOT'
PATH_FIGURE_2 = os.path.join(PATH_FIGURES, NAME_TIME + '_' + NAME_FIGURE_2 + EXT_FIG)
plt.savefig( PATH_FIGURE_2 , dpi=100 )

# %%
##Kruskal Willis Test

results_KW = np.zeros((7,2))

results_KW[0] = stats.kruskal(df['Alcohol'].notnull(),df['Ninguna'].notnull())
results_KW[1] = stats.kruskal(df['Cigarrillo'].notnull(),df['Ninguna'].notnull())
results_KW[2] = stats.kruskal(df['Café'].notnull(),df['Ninguna'].notnull())
results_KW[3] = stats.kruskal(df['Chocolate'].notnull(),df['Ninguna'].notnull())
results_KW[4] = stats.kruskal(df['Marihuana'].notnull(),df['Ninguna'].notnull())
results_KW[5] = stats.kruskal(df['Bebida energizante'].notnull(),df['Ninguna'].notnull())

results_KW[6] = stats.kruskal(df['Alcohol'].notnull(),df[
 'Cigarrillo'].notnull(),df[
 'Café'].notnull(),df[
 'Chocolate'].notnull(),df[
 'Ninguna'].notnull(),df[
 'Marihuana'].notnull(),df[
 'Bebida energizante'].notnull())

#Creating pandas dataframe from numpy array
df_KW = pd.DataFrame({'Statistic':results_KW[:,0],'p-value':results_KW[:,1]})
df_KW.rename(index={0:'Alcohol',1:'Cigarrillo',2:'Café',3:'Chocholate',4:'Marihuana',5:'Bebida energizante', 6: 'Todos'})
print(df_KW)

# %%
## Mann Whitney Test
stats.mannwhitneyu(df['Café'],df['Ninguna'])

