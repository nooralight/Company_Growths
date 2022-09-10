import pandas as pd
from download_Annual import Accounting_Info_Annual as AI

class Find_Growth_Annual:
    
    def __init__(self):
        self.obj = AI()
    
    
    def revenue_growth(self, symbol_name):
        rev_growth_dict = []
        df_income,_ = self.obj.getIncomeStatements(symbol_name)
        i=0
        df_length = len(df_income)-1
        for index in range(df_length+1):          
            if i==df_length:
                ########********
                if df_income["revenue"][index] !=0:
                    prev_rev = float(df_income["revenue"][index])
                    curr_rev = float(df_income["revenue"][index])
                    growth_percent = ((curr_rev-prev_rev)/prev_rev)*100
                    growth = (curr_rev-prev_rev)/prev_rev
                    
                    date = df_income["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"Revenue_Growth_Percant":growth_percent,"Revenue_Growth":growth}
                    rev_growth_dict.append(dic)
            else:
                prev_rev= float(df_income["revenue"][i+1])
                curr_rev = float(df_income["revenue"][i])
                ######## *******
                if prev_rev!=0.0:
                    growth_percent = ((curr_rev-prev_rev)/prev_rev)*100
                    growth = (curr_rev-prev_rev)/prev_rev
                    
                    date = df_income["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"Revenue_Growth_Percant":growth_percent,"Revenue_Growth":growth}
                    rev_growth_dict.append(dic)
            i+=1
        return rev_growth_dict
    
    def earning_growth(self , symbol_name):
        earning_growth_dict = []
        df_income,_ = self.obj.getIncomeStatements(symbol_name)
        i=0
        df_length = len(df_income)-1
        for index in range(df_length+1):          
            if i==df_length:
                if df_income["netIncome"][index] !=0:
                    prev_income = float(df_income["netIncome"][index])
                    curr_income = float(df_income["netIncome"][index])
                    growth_percent = ((curr_income-prev_income)/prev_income)*100
                    growth = (curr_income-prev_income)/prev_income
                    
                    date = df_income["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"Earning_Growth_Percant":growth_percent,"Earning_Growth":growth}
                    earning_growth_dict.append(dic)
            else:
                prev_income= float(df_income["netIncome"][i+1])
                curr_income = float(df_income["netIncome"][i])
                if prev_income!=0.0:
                    growth_percent = ((curr_income-prev_income)/prev_income)*100
                    growth = (curr_income-prev_income)/prev_income
                    
                    date = df_income["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"Earning_Growth_Percant":growth_percent,"Earning_Growth":growth}
                    earning_growth_dict.append(dic)
            i+=1
        return earning_growth_dict
    
    def fcf_growth(self, symbol_name):
        fcf_growth_dict = []
        df_cashflow,_ = self.obj.getAnnualCashFlow(symbol_name)
        i=0
        df_length = len(df_cashflow)-1
        for index in range(df_length+1):          
            if i==df_length:
                if df_cashflow["freeCashFlow"][index]!=0:
                    prev_fcf = float(df_cashflow["freeCashFlow"][index])
                    curr_fcf = float(df_cashflow["freeCashFlow"][index])
                    growth_percent = ((curr_fcf-prev_fcf)/prev_fcf)*100
                    growth = (curr_fcf-prev_fcf)/prev_fcf
                    
                    date = df_cashflow["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"freeCashFlow_Growth_Percant":growth_percent, "freeCashFlow_Growth":growth}
                    fcf_growth_dict.append(dic)
            else:
                prev_fcf = float(df_cashflow["freeCashFlow"][i+1])
                curr_fcf = float(df_cashflow["freeCashFlow"][i])
                if prev_fcf !=0.0:
                    growth_percent = ((curr_fcf-prev_fcf)/prev_fcf)*100
                    growth = (curr_fcf-prev_fcf)/prev_fcf
                    
                    date = df_cashflow["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"freeCashFlow_Growth_Percant":growth_percent, "freeCashFlow_Growth":growth}
                    fcf_growth_dict.append(dic)
            i+=1
        return fcf_growth_dict
    
    def marketSize_growth(self, symbol_name):
        #totalStockholdersEquity
        ms_growth_dict = []
        df_balance,_ = self.obj.getAnnualBalanceSheet(symbol_name)
        i=0
        df_length = len(df_balance)-1
        for index in range(df_length+1):          
            if i==df_length:
                if df_balance["totalStockholdersEquity"][index]!=0: 
                    prev_ms = float(df_balance["totalStockholdersEquity"][index])
                    curr_ms = float(df_balance["totalStockholdersEquity"][index])
                    growth_percent = ((curr_ms-prev_ms)/prev_ms)*100
                    growth = (curr_ms-prev_ms)/prev_ms
                    
                    date = df_balance["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"MarketSize_Growth_Percant":growth_percent,"MarketSize_Growth":growth}
                    ms_growth_dict.append(dic)
            else:
                prev_ms = float(df_balance["totalStockholdersEquity"][i+1])
                curr_ms = float(df_balance["totalStockholdersEquity"][i])
                if prev_ms!=0.0:
                    growth_percent = ((curr_ms-prev_ms)/prev_ms)*100
                    growth = (curr_ms-prev_ms)/prev_ms
                    
                    
                    date = df_balance["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"MarketSize_Growth_Percant":growth_percent,"MarketSize_Growth":growth}
                    ms_growth_dict.append(dic)
            i+=1
        return ms_growth_dict
        
                
    
    
#rev_growth = Find_Growth().revenue_growth("AAPL")
'''
earning_growth = Find_Revenue().earning_growth("AAPL")
fcf_growth = Find_Revenue().fcf_growth("AAPL")
ms_growth = Find_Revenue().marketSize_growth("AAPL")'''