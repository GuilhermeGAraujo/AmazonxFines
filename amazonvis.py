# -*- coding: utf-8 -*-

import pandas as pd
import tabula
from functools import reduce
 
multas_dict = {}

for i in range(2010,2021):
    key ='multas'+str(i)
    path = key+'.pdf'
    #extrating the data from the pdf
    dfs = tabula.read_pdf(path,pages = 'all')
    single_df = reduce(lambda left,right: pd.concat([left,right]),dfs)
# =============================================================================
#   I'm only interested in the total numbers of fines and in the total ammount 
#   in BRL of the fines so I only the need the ammount datapoint of the messy 
#   data.
# =============================================================================
    single_df = single_df.iloc[:,7:10]
    single_df.dropna(how = 'all', inplace = True)
    single_df = single_df.astype(str)
    multas = [item for lst in single_df.values for item in lst if item.endswith(',00')]
    multas_dict[key] = multas
    
import pickle

with open ('multas.pkl','wb') as f:
        pickle.dump(multas_dict,f)

             


