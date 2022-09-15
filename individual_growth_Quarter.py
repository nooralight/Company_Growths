# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 15:13:06 2022

@author: noorm
"""

import pandas as pd
import dow_jones
import nasdaq
import sp500sectors
from find_growth_Quarter import Find_Growth_Quarter as FG_Q


class Individual_Growth_view:
    
    def __init__(self):
        self.fg_q = FG_Q()
        _,_,self.list_of_symbol_dow = dow_jones.getting_subsectors()
        _,_,self.list_of_symbol_sp = sp500sectors.getting_subsectors()
        _,_,self.list_of_symbol_nas = nasdaq.getting_subsectors()
    
    def individual_revenue_growth_dowjones(self):
        
        growth_dictionary = []
        for index in range(10):
            temp = FG_Q().revenue_growth(self.list_of_symbol_dow[index])
            state = ""
            if temp[0]["Revenue_Growth_Percant"]<temp[1]["Revenue_Growth_Percant"] and temp[1]["Revenue_Growth_Percant"]<temp[2]["Revenue_Growth_Percant"]:
                state = "danger"
            elif temp[0]["Revenue_Growth_Percant"]<temp[1]["Revenue_Growth_Percant"] and temp[1]["Revenue_Growth_Percant"]>temp[2]["Revenue_Growth_Percant"]:
                state = "decreasing"
            elif temp[0]["Revenue_Growth_Percant"]>temp[1]["Revenue_Growth_Percant"]:
                state = "rising"
            temp_arr = []
            for i in temp:
                temp_arr.append(i["Revenue_Growth_Percant"])
            growth_dictionary.append({"Symbol":self.list_of_symbol_dow[index],"state":state, "individual_revenue":temp_arr})
        return growth_dictionary

    def individual_earning_growth_dowjones(self):
        #_,_,list_of_symbol_dow = dow_jones.getting_subsectors()
        growth_dictionary = []
        for index in range(10):
            temp = FG_Q().earning_growth(self.list_of_symbol_dow[index])
            state = ""
            if temp[0]["Earning_Growth_Percant"]<temp[1]["Earning_Growth_Percant"] and temp[1]["Earning_Growth_Percant"]<temp[2]["Earning_Growth_Percant"]:
                state = "danger"
            elif temp[0]["Earning_Growth_Percant"]<temp[1]["Earning_Growth_Percant"] and temp[1]["Earning_Growth_Percant"]>temp[2]["Earning_Growth_Percant"]:
                state = "decreasing"
            elif temp[0]["Earning_Growth_Percant"]>temp[1]["Earning_Growth_Percant"]:
                state = "rising"
            temp_arr = []
            for i in temp:
                temp_arr.append(i["Earning_Growth_Percant"])
            growth_dictionary.append({"Symbol":self.list_of_symbol_dow[index],"state":state,"individual_earning":temp_arr})
        return growth_dictionary
    
    def individual_fcf_growth_dowjones(self):
        #_,_,list_of_symbol_dow = dow_jones.getting_subsectors()
        growth_dictionary = []
        for index in range(10):
            temp = FG_Q().fcf_growth(self.list_of_symbol_dow[index])
            state = ""
            if temp[0]["freeCashFlow_Growth_Percant"]<temp[1]["freeCashFlow_Growth_Percant"] and temp[1]["freeCashFlow_Growth_Percant"]<temp[2]["freeCashFlow_Growth_Percant"]:
                state = "danger"
            elif temp[0]["freeCashFlow_Growth_Percant"]<temp[1]["freeCashFlow_Growth_Percant"] and temp[1]["freeCashFlow_Growth_Percant"]>temp[2]["freeCashFlow_Growth_Percant"]:
                state = "decreasing"
            elif temp[0]["freeCashFlow_Growth_Percant"]>temp[1]["freeCashFlow_Growth_Percant"]:
                state = "rising"
            temp_arr = []
            for i in temp:
                temp_arr.append(i["freeCashFlow_Growth_Percant"])
            growth_dictionary.append({"Symbol":self.list_of_symbol_dow[index],"state":state,"individual_fcf":temp_arr})
        return growth_dictionary  
    
    
    def individual_eps_growth_dowjones(self):
        #_,_,list_of_symbol_dow = dow_jones.getting_subsectors()
        growth_dictionary = []
        for index in range(10):
            temp = FG_Q().eps_margin_growth(self.list_of_symbol_dow[index])
            state = ""
            if temp[0]["eps_Growth_Percant"]<temp[1]["eps_Growth_Percant"] and temp[1]["eps_Growth_Percant"]<temp[2]["eps_Growth_Percant"]:
                state = "danger"
            elif temp[0]["eps_Growth_Percant"]<temp[1]["eps_Growth_Percant"] and temp[1]["eps_Growth_Percant"]>temp[2]["eps_Growth_Percant"]:
                state = "decreasing"
            elif temp[0]["eps_Growth_Percant"]>temp[1]["eps_Growth_Percant"]:
                state = "rising"
            temp_arr = []
            for i in temp:
                temp_arr.append(i["eps_Growth_Percant"])
            growth_dictionary.append({"Symbol":self.list_of_symbol_dow[index],"state":state,"individual_eps":temp_arr})
        return growth_dictionary
    

    def individual_gross_growth_dowjones(self):
        #_,_,list_of_symbol_dow = dow_jones.getting_subsectors()
        growth_dictionary = []
        for index in range(10):
            temp = FG_Q().gross_margin_growth(self.list_of_symbol_dow[index])
            state = ""
            if temp[0]["grossProfit_Growth_Percant"]<temp[1]["grossProfit_Growth_Percant"] and temp[1]["grossProfit_Growth_Percant"]<temp[2]["grossProfit_Growth_Percant"]:
                state = "danger"
            elif temp[0]["grossProfit_Growth_Percant"]<temp[1]["grossProfit_Growth_Percant"] and temp[1]["grossProfit_Growth_Percant"]>temp[2]["grossProfit_Growth_Percant"]:
                state = "decreasing"
            elif temp[0]["grossProfit_Growth_Percant"]>temp[1]["grossProfit_Growth_Percant"]:
                state = "rising"
            temp_arr = []
            for i in temp:
                temp_arr.append(i["grossProfit_Growth_Percant"])
            growth_dictionary.append({"Symbol":self.list_of_symbol_dow[index],"state":state,"individual_grossMargin":temp_arr})
        return growth_dictionary


    def individual_operating_growth_dowjones(self):
        #_,_,list_of_symbol_dow = dow_jones.getting_subsectors()
        growth_dictionary = []
        for index in range(10):
            temp = FG_Q().operating_margin_growth(self.list_of_symbol_dow[index])
            state = ""
            if temp[0]["operatingIncome_Growth_Percant"]<temp[1]["operatingIncome_Growth_Percant"] and temp[1]["operatingIncome_Growth_Percant"]<temp[2]["operatingIncome_Growth_Percant"]:
                state = "danger"
            elif temp[0]["operatingIncome_Growth_Percant"]<temp[1]["operatingIncome_Growth_Percant"] and temp[1]["operatingIncome_Growth_Percant"]>temp[2]["operatingIncome_Growth_Percant"]:
                state = "decreasing"
            elif temp[0]["operatingIncome_Growth_Percant"]>temp[1]["operatingIncome_Growth_Percant"]:
                state = "rising"
            temp_arr = []
            for i in temp:
                temp_arr.append(i["operatingIncome_Growth_Percant"])
            growth_dictionary.append({"Symbol":self.list_of_symbol_dow[index],"state":state,"individual_operatingMargin":temp_arr})
        return growth_dictionary



    def individual_netProfit_growth_dowjones(self):
        #_,_,list_of_symbol_dow = dow_jones.getting_subsectors()
        growth_dictionary = []
        for index in range(10):
            temp = FG_Q().netProfit_margin_growth(self.list_of_symbol_dow[index])
            state = ""
            if temp[0]["netProfit_Growth_Percant"]<temp[1]["netProfit_Growth_Percant"] and temp[1]["netProfit_Growth_Percant"]<temp[2]["netProfit_Growth_Percant"]:
                state = "danger"
            elif temp[0]["netProfit_Growth_Percant"]<temp[1]["netProfit_Growth_Percant"] and temp[1]["netProfit_Growth_Percant"]>temp[2]["netProfit_Growth_Percant"]:
                state = "decreasing"
            elif temp[0]["netProfit_Growth_Percant"]>temp[1]["netProfit_Growth_Percant"]:
                state = "rising"
            temp_arr = []
            for i in temp:
                temp_arr.append(i["netProfit_Growth_Percant"])
            growth_dictionary.append({"Symbol":self.list_of_symbol_dow[index],"state":state,"individual_netProfitMargin":temp_arr})
        return growth_dictionary

        


    def individual_revenue_growth_sp(self):
        
        growth_dictionary = []
        for index in range(10):
            temp = FG_Q().revenue_growth(self.list_of_symbol_sp[index])
            state = ""
            if temp[0]["Revenue_Growth_Percant"]<temp[1]["Revenue_Growth_Percant"] and temp[1]["Revenue_Growth_Percant"]<temp[2]["Revenue_Growth_Percant"]:
                state = "danger"
            elif temp[0]["Revenue_Growth_Percant"]<temp[1]["Revenue_Growth_Percant"] and temp[1]["Revenue_Growth_Percant"]>temp[2]["Revenue_Growth_Percant"]:
                state = "decreasing"
            elif temp[0]["Revenue_Growth_Percant"]>temp[1]["Revenue_Growth_Percant"]:
                state = "rising"
            temp_arr = []
            for i in temp:
                temp_arr.append(i["Revenue_Growth_Percant"])
            growth_dictionary.append({"Symbol":self.list_of_symbol_sp[index],"state":state, "individual_revenue":temp_arr})
        return growth_dictionary

    def individual_earning_growth_sp(self):
        #_,_,list_of_symbol = dow_jones.getting_subsectors()
        growth_dictionary = []
        for index in range(10):
            temp = FG_Q().earning_growth(self.list_of_symbol_sp[index])
            state = ""
            if temp[0]["Earning_Growth_Percant"]<temp[1]["Earning_Growth_Percant"] and temp[1]["Earning_Growth_Percant"]<temp[2]["Earning_Growth_Percant"]:
                state = "danger"
            elif temp[0]["Earning_Growth_Percant"]<temp[1]["Earning_Growth_Percant"] and temp[1]["Earning_Growth_Percant"]>temp[2]["Earning_Growth_Percant"]:
                state = "decreasing"
            elif temp[0]["Earning_Growth_Percant"]>temp[1]["Earning_Growth_Percant"]:
                state = "rising"
            temp_arr = []
            for i in temp:
                temp_arr.append(i["Earning_Growth_Percant"])
            growth_dictionary.append({"Symbol":self.list_of_symbol_sp[index],"state":state,"individual_earning":temp_arr})
        return growth_dictionary
    
    def individual_fcf_growth_sp(self):
        #_,_,list_of_symbol_sp = dow_jones.getting_subsectors()
        growth_dictionary = []
        for index in range(10):
            temp = FG_Q().fcf_growth(self.list_of_symbol_sp[index])
            state = ""
            if temp[0]["freeCashFlow_Growth_Percant"]<temp[1]["freeCashFlow_Growth_Percant"] and temp[1]["freeCashFlow_Growth_Percant"]<temp[2]["freeCashFlow_Growth_Percant"]:
                state = "danger"
            elif temp[0]["freeCashFlow_Growth_Percant"]<temp[1]["freeCashFlow_Growth_Percant"] and temp[1]["freeCashFlow_Growth_Percant"]>temp[2]["freeCashFlow_Growth_Percant"]:
                state = "decreasing"
            elif temp[0]["freeCashFlow_Growth_Percant"]>temp[1]["freeCashFlow_Growth_Percant"]:
                state = "rising"
            temp_arr = []
            for i in temp:
                temp_arr.append(i["freeCashFlow_Growth_Percant"])
            growth_dictionary.append({"Symbol":self.list_of_symbol_sp[index],"state":state,"individual_fcf":temp_arr})
        return growth_dictionary 
    
    
    
    def individual_revenue_growth_nas(self):
        
        growth_dictionary = []
        for index in range(10):
            temp = FG_Q().revenue_growth(self.list_of_symbol_nas[index])
            state = ""
            if temp[0]["Revenue_Growth_Percant"]<temp[1]["Revenue_Growth_Percant"] and temp[1]["Revenue_Growth_Percant"]<temp[2]["Revenue_Growth_Percant"]:
                state = "danger"
            elif temp[0]["Revenue_Growth_Percant"]<temp[1]["Revenue_Growth_Percant"] and temp[1]["Revenue_Growth_Percant"]>temp[2]["Revenue_Growth_Percant"]:
                state = "decreasing"
            elif temp[0]["Revenue_Growth_Percant"]>temp[1]["Revenue_Growth_Percant"]:
                state = "rising"
            temp_arr = []
            for i in temp:
                temp_arr.append(i["Revenue_Growth_Percant"])
            growth_dictionary.append({"Symbol":self.list_of_symbol_nas[index],"state":state, "individual_revenue":temp_arr})
        return growth_dictionary

    def individual_earning_growth_nas(self):
        #_,_,list_of_symbol = dow_jones.getting_subsectors()
        growth_dictionary = []
        for index in range(10):
            temp = FG_Q().earning_growth(self.list_of_symbol_nas[index])
            state = ""
            if temp[0]["Earning_Growth_Percant"]<temp[1]["Earning_Growth_Percant"] and temp[1]["Earning_Growth_Percant"]<temp[2]["Earning_Growth_Percant"]:
                state = "danger"
            elif temp[0]["Earning_Growth_Percant"]<temp[1]["Earning_Growth_Percant"] and temp[1]["Earning_Growth_Percant"]>temp[2]["Earning_Growth_Percant"]:
                state = "decreasing"
            elif temp[0]["Earning_Growth_Percant"]>temp[1]["Earning_Growth_Percant"]:
                state = "rising"
            temp_arr = []
            for i in temp:
                temp_arr.append(i["Earning_Growth_Percant"])
            growth_dictionary.append({"Symbol":self.list_of_symbol_nas[index],"state":state,"individual_earning":temp_arr})
        return growth_dictionary
    
    def individual_fcf_growth_nas(self):
        #_,_,list_of_symbol_nas = dow_jones.getting_subsectors()
        growth_dictionary = []
        for index in range(10):
            temp = FG_Q().fcf_growth(self.list_of_symbol_nas[index])
            state = ""
            if temp[0]["freeCashFlow_Growth_Percant"]<temp[1]["freeCashFlow_Growth_Percant"] and temp[1]["freeCashFlow_Growth_Percant"]<temp[2]["freeCashFlow_Growth_Percant"]:
                state = "danger"
            elif temp[0]["freeCashFlow_Growth_Percant"]<temp[1]["freeCashFlow_Growth_Percant"] and temp[1]["freeCashFlow_Growth_Percant"]>temp[2]["freeCashFlow_Growth_Percant"]:
                state = "decreasing"
            elif temp[0]["freeCashFlow_Growth_Percant"]>temp[1]["freeCashFlow_Growth_Percant"]:
                state = "rising"
            temp_arr = []
            for i in temp:
                temp_arr.append(i["freeCashFlow_Growth_Percant"])
            growth_dictionary.append({"Symbol":self.list_of_symbol_nas[index],"state":state,"individual_fcf":temp_arr})
        return growth_dictionary 
'''
dow_testing_revenue_Quarter = individual_Growth_view().individual_revenue_growth_dowjones()
dow_testing_earning_Quarter = individual_Growth_view().individual_earning_growth_dowjones()
dow_testing_fcf_Quarter = individual_Growth_view().individual_fcf_growth_dowjones()

sp_testing_revenue_Quarter = individual_Growth_view().individual_revenue_growth_sp()
sp_testing_earning_Quarter = individual_Growth_view().individual_earning_growth_sp()
sp_testing_fcf_Quarter = individual_Growth_view().individual_fcf_growth_sp()


nas_testing_revenue_Quarter = individual_Growth_view().individual_revenue_growth_nas()
nas_testing_earning_Quarter = individual_Growth_view().individual_earning_growth_nas()
nas_testing_fcf_Quarter = individual_Growth_view().individual_fcf_growth_nas()
'''

dow_testing_eps_Quarter = Individual_Growth_view().individual_eps_growth_dowjones()
dow_testing_gross_Quarter = Individual_Growth_view().individual_gross_growth_dowjones()
dow_testing_netIncome_Quarter = Individual_Growth_view().individual_netProfit_growth_dowjones() 
dow_testing_operating_Quarter = Individual_Growth_view().individual_operating_growth_dowjones()







    
    