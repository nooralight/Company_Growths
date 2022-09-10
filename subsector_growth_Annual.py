# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 15:41:45 2022

@author: noorm
"""
from subsector_marketsize_Annual import Subsector_Growth_Annual as SG_A

class Subsector_Growth_view:
    
    def __init__(self):
        self.sg_a = SG_A()
        _,_,self.list_of_symbol_dow = dow_jones.getting_subsectors()
        _,_,self.list_of_symbol_sp = sp500sectors.getting_subsectors()
        _,_,self.list_of_symbol_nas = nasdaq.getting_subsectors()

    def subsector_revenue_growth_sp(self):
        url = "https://financialmodelingprep.com/api/v3/sp500_constituent?apikey="+"2b2bbacbc149bcba58903f591ae3d3c8"
        url_subsectors= url
        source_subsectors =  urllib.request.urlopen(url_subsectors).read()
        list_of_incomeStatement = json.loads(source_subsectors)
        df = pd.DataFrame(list_of_incomeStatement)
        df_new = df.iloc[:,[0,1,3]]
        arr = df_new["subSector"].tolist()
        list_of_subsectors = list(set(arr))
        return list_of_subsectors, df_new
    
s = Subsector_Growth_view().subsector_revenue_growth_sp()
        
        