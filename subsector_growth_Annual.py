# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 15:41:45 2022

@author: noorm
"""
import dow_jones
import nasdaq
import sp500sectors
from subsector_marketsize_Annual import Subsector_Growth_Annual as SG_A

class Subsector_Growth_view:
    
    def __init__(self):
        self.sg_a = SG_A()
        self.df_subsector_dow,_,self.list_of_symbol_dow = dow_jones.getting_subsectors()
        self.df_subsector_sp,_,self.list_of_symbol_sp = sp500sectors.getting_subsectors()
        self.df_subsector_nas,_,self.list_of_symbol_nas = nasdaq.getting_subsectors()

    def subsector_growth_sp(self):
        list_of_symbol = self.list_of_symbol_sp
        
        subsector_dict = []
        for index in range(3):
            rev_percant, rev_state = self.sg_a.subsector_wise_revGrowth(list_of_symbol[index],self.df_subsector_sp)
            earning_percant, earning_state = self.sg_a.subsector_wise_earnGrowth(list_of_symbol[index],self.df_subsector_sp)
            fcf_percant, fcf_state = self.sg_a.subsector_wise_fcfGrowth(list_of_symbol[index],self.df_subsector_sp)
            netIncome_percant, netIncome_state = self.sg_a.subsector_wise_netIncomeGrowth(list_of_symbol[index],self.df_subsector_sp)
            gross_percant, gross_state = self.sg_a.subsector_wise_grossGrowth(list_of_symbol[index],self.df_subsector_sp)
            eps_percant, eps_state = self.sg_a.subsector_wise_epsGrowth(list_of_symbol[index],self.df_subsector_sp)
            operating_percant, operating_state = self.sg_a.subsector_wise_operatingGrowth(list_of_symbol[index],self.df_subsector_sp)
            
            subsector_dict.append({"Symbol":list_of_symbol[index],"RevenueGrowth":rev_percant,"Rank_Revenue":rev_state,"EarningGrowth":earning_percant,"Rank_Earning":earning_state,
                                   "Fcf_Growth":fcf_percant,"Rank_Fcf":fcf_state,"netIncome_Growth":netIncome_percant,"Rank_netIncome":netIncome_state,
                                   "Gross_Growth":gross_percant,"Rank_Gross":gross_state,"eps_Growth":eps_percant,"Rank_EPS":eps_state,
                                   "operating_Growth":operating_percant,"Rank_Operating":operating_state})
        return subsector_dict
    
    
    
    
    def subsector_growth_dow(self):
        list_of_symbol = self.list_of_symbol_dow
        
        subsector_dict = []
        for index in range(3):
            rev_percant, rev_state = self.sg_a.subsector_wise_revGrowth(list_of_symbol[index],self.df_subsector_dow)
            earning_percant, earning_state = self.sg_a.subsector_wise_earnGrowth(list_of_symbol[index],self.df_subsector_dow)
            fcf_percant, fcf_state = self.sg_a.subsector_wise_fcfGrowth(list_of_symbol[index],self.df_subsector_dow)
            netIncome_percant, netIncome_state = self.sg_a.subsector_wise_netIncomeGrowth(list_of_symbol[index],self.df_subsector_dow)
            gross_percant, gross_state = self.sg_a.subsector_wise_grossGrowth(list_of_symbol[index],self.df_subsector_dow)
            eps_percant, eps_state = self.sg_a.subsector_wise_epsGrowth(list_of_symbol[index],self.df_subsector_dow)
            operating_percant, operating_state = self.sg_a.subsector_wise_operatingGrowth(list_of_symbol[index],self.df_subsector_dow)
            
            subsector_dict.append({"Symbol":list_of_symbol[index],"RevenueGrowth":rev_percant,"Rank_Revenue":rev_state,"EarningGrowth":earning_percant,"Rank_Earning":earning_state,
                                   "Fcf_Growth":fcf_percant,"Rank_Fcf":fcf_state,"netIncome_Growth":netIncome_percant,"Rank_netIncome":netIncome_state,
                                   "Gross_Growth":gross_percant,"Rank_Gross":gross_state,"eps_Growth":eps_percant,"Rank_EPS":eps_state,
                                   "operating_Growth":operating_percant,"Rank_Operating":operating_state})
        return subsector_dict
    
    
    
    def subsector_growth_nas(self):
        list_of_symbol = self.list_of_symbol_nas
        
        subsector_dict = []
        for index in range(3):
            rev_percant, rev_state = self.sg_a.subsector_wise_revGrowth(list_of_symbol[index],self.df_subsector_nas)
            earning_percant, earning_state = self.sg_a.subsector_wise_earnGrowth(list_of_symbol[index],self.df_subsector_nas)
            fcf_percant, fcf_state = self.sg_a.subsector_wise_fcfGrowth(list_of_symbol[index],self.df_subsector_nas)
            netIncome_percant, netIncome_state = self.sg_a.subsector_wise_netIncomeGrowth(list_of_symbol[index],self.df_subsector_nas)
            gross_percant, gross_state = self.sg_a.subsector_wise_grossGrowth(list_of_symbol[index],self.df_subsector_nas)
            eps_percant, eps_state = self.sg_a.subsector_wise_epsGrowth(list_of_symbol[index],self.df_subsector_nas)
            operating_percant, operating_state = self.sg_a.subsector_wise_operatingGrowth(list_of_symbol[index],self.df_subsector_nas)
            
            subsector_dict.append({"Symbol":list_of_symbol[index],"RevenueGrowth":rev_percant,"Rank_Revenue":rev_state,"EarningGrowth":earning_percant,"Rank_Earning":earning_state,
                                   "Fcf_Growth":fcf_percant,"Rank_Fcf":fcf_state,"netIncome_Growth":netIncome_percant,"Rank_netIncome":netIncome_state,
                                   "Gross_Growth":gross_percant,"Rank_Gross":gross_state,"eps_Growth":eps_percant,"Rank_EPS":eps_state,
                                   "operating_Growth":operating_percant,"Rank_Operating":operating_state})
        return subsector_dict
print("sp ..")   
sp_growth_Annual = Subsector_Growth_view().subsector_growth_sp()
'''
print("nasdaq ..")
nasdaq_growth_Annual = Subsector_Growth_view().subsector_growth_nas()
print("Dow ..")
dow_growth_Annual = Subsector_Growth_view().subsector_growth_dow()
'''