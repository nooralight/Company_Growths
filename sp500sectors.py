# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 11:48:34 2022

@author: noorm
"""

import urllib.request
import pandas as pd
import json

def getting_subsectors():
    url_subsectors= "https://financialmodelingprep.com/api/v3/sp500_constituent?apikey="+"2b2bbacbc149bcba58903f591ae3d3c8"
    source_subsectors =  urllib.request.urlopen(url_subsectors).read()
    list_of_incomeStatement = json.loads(source_subsectors)
    df = pd.DataFrame(list_of_incomeStatement)
    df_new = df.iloc[:,[0,1,3]]
    arr = df_new["subSector"].tolist()
    list_symbol = df_new["symbol"].tolist()
    list_of_subsectors = list(set(arr))
    return df_new , list_of_subsectors, list_symbol



company_info,subsectors, symbols = getting_subsectors()