import pandas as pd
from download_Annual import Accounting_Info as AI
ob = AI()
class Find_Multiple:
    
    def __init__(self):
        pass
    
        
    def multiple_of_Revenue(self,symbol_name):
        revenue_dictionary = []
        df_ev,_ = ob.getEV(symbol_name)
        df_income,_ = ob.getIncomeStatements(symbol_name)
        
        arr_of_multiple_revenue=[]
        for index in range(len(df_ev)):
            ev= float(df_ev["enterpriseValue"][index])
            rev = float(df_income["revenue"][index])
            multiple = ev/rev
            arr_of_multiple_revenue.append(multiple)
            
            date = df_ev["date"][index]
            dic = {"Date":str(date),"Revenue_Multiple":multiple}
            revenue_dictionary.append(dic)
        max_multiple = max(arr_of_multiple_revenue)
        min_multiple = min(arr_of_multiple_revenue)
        mean_multiple = (min_multiple+max_multiple)/2
        
        state_multiple_revenue = {"minimum_multiRev":min_multiple,"max_multiRev":max_multiple,"mean_multiRev":mean_multiple}
        if revenue_dictionary[0]['Revenue_Multiple']>=mean_multiple:
            print("Over valued")
            state_multiple_revenue["value"] = "OverValued"
        else:
            print("Under valued")
            state_multiple_revenue["value"] = "UnderValued"
        return revenue_dictionary, state_multiple_revenue
    
    def multiple_of_FCF(self,symbol_name):
        fcf_dictionary = []
        df_ev,_ = ob.getEV(symbol_name)
        df_cashflow,_ = ob.getAnnualCashFlow(symbol_name)
        
        arr_of_multiple_fcf=[]
        for index in range(len(df_cashflow)):
            mc= float(df_ev["marketCapitalization"][index])
            fcf = float(df_cashflow["freeCashFlow"][index])
            multiple = mc/fcf
            arr_of_multiple_fcf.append(multiple)
            
            date = df_ev["date"][index]
            dic = {"Date":str(date),"FCF_Multiple":multiple }
            fcf_dictionary.append(dic)
        max_multiple = max(arr_of_multiple_fcf)
        min_multiple = min(arr_of_multiple_fcf)
        mean_multiple = (min_multiple+max_multiple)/2
        
        state_multiple_fcf = {"minimum_multiFCF":min_multiple,"max_multiFCF":max_multiple,"mean_multiFCF":mean_multiple}
        if fcf_dictionary[0]['FCF_Multiple']>=mean_multiple:
            print("Over valued")
            state_multiple_fcf["value"] = "OverValued"
        else:
            print("Under valued")
            state_multiple_fcf["value"] = "UnderValued"
            
        return fcf_dictionary, state_multiple_fcf
    
    
    
    def multiple_of_EBITDA(self, symbol_name):
        ebitda_dictionary = []
        df_ev,_ = ob.getEV(symbol_name)
        df_income,_ = ob.getIncomeStatements(symbol_name)
        
        arr_of_multiple_EBITDA=[]
        for index in range(len(df_ev)):
            ev= float(df_ev["enterpriseValue"][index])
            ebitda = float(df_income["ebitda"][index])
            multiple = ev/ebitda
            arr_of_multiple_EBITDA.append(multiple)
            date = df_ev["date"][index]
            dic = {"Date":str(date),"EBITDA_Multiple":multiple }
            ebitda_dictionary.append(dic)
        
        max_multiple = max(arr_of_multiple_EBITDA)
        min_multiple = min(arr_of_multiple_EBITDA)
        mean_multiple = (min_multiple+max_multiple)/2
        
        state_multiple_EBITDA = {"minimum_multiEBITDA":min_multiple,"max_multiEBITDA":max_multiple,"mean_multiEBITDA":mean_multiple}
        if ebitda_dictionary[0]['EBITDA_Multiple']>=mean_multiple:
            print("Over valued")
            state_multiple_EBITDA["value"] = "OverValued"
        else:
            print("Under valued")
            state_multiple_EBITDA["value"] = "UnderValued"
            
        return ebitda_dictionary, state_multiple_EBITDA
    
    def multiple_of_GMV(self, symbol_name):
        gmv_dictionary = []
        df_ev,_ = ob.getEV(symbol_name)
        df_income,_ = ob.getIncomeStatements(symbol_name)
        
        arr_of_multiple_GMV=[]
        for index in range(len(df_ev)):
            mc= float(df_ev["marketCapitalization"][index])
            rev = float(df_income["revenue"][index])
            multiple = mc/rev
            arr_of_multiple_GMV.append(multiple)
            date = df_ev["date"][index]
            dic = {"Date":str(date),"GMV_Multiple":multiple }
            gmv_dictionary.append(dic)
            
        max_multiple = max(arr_of_multiple_GMV)
        min_multiple = min(arr_of_multiple_GMV)
        mean_multiple = (min_multiple+max_multiple)/2
        
        state_multiple_GMV = {"minimum_multiGMV":min_multiple,"max_multiGMV":max_multiple,"mean_multiGMV":mean_multiple}
        if gmv_dictionary[0]['GMV_Multiple']>=mean_multiple:
            print("Over valued")
            state_multiple_GMV["value"] = "OverValued"
        else:
            print("Under valued")
            state_multiple_GMV["value"] = "UnderValued"
            
        return gmv_dictionary, state_multiple_GMV
        
        
        

#symbols = Find_Multiple("symbol&Companies.csv").getSymbols()
rev_multiple, rev_states = Find_Multiple().multiple_of_Revenue("AAPL")
fcf_multiple, fcf_states = Find_Multiple().multiple_of_FCF("AAPL")
ebitda_multiple, ebitda_states = Find_Multiple().multiple_of_EBITDA("AAPL")
gmv_multiple, gmv_states = Find_Multiple().multiple_of_GMV("AAPL")

"""fcf_multiple = Find_Multiple("AAPL").multiple_of_FCF()
ebitda_multiple = Find_Multiple("AAPL").multiple_of_EBITDA()
gmv_multiple = Find_Multiple("AAPL").multiple_of_GMV()"""
'''




