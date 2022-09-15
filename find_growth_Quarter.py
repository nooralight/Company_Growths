import pandas as pd
from download_Quarter import Accounting_Info_Quarter as AI_Q

class Find_Growth_Quarter:
    
    def __init__(self):
        self.obj = AI_Q()
    
    
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
                    dic = {"Date":str(date),"Revenue_Growth_Percant":growth_percent,"Revenue_Growth":growth}
                    rev_growth_dict.append(dic)
            else:
                prev_rev= float(df_income["revenue"][i+1])
                curr_rev = float(df_income["revenue"][i])
                ######## *******
                if prev_rev!=0.0:
                    growth_percent = ((curr_rev-prev_rev)/prev_rev)*100
                    growth = (curr_rev-prev_rev)/prev_rev
                    
                    date = df_income["date"][index]
                    dic = {"Date":str(date),"Revenue_Growth_Percant":growth_percent,"Revenue_Growth":growth}
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
                    dic = {"Date":str(date),"Earning_Growth_Percant":growth_percent,"Earning_Growth":growth}
                    earning_growth_dict.append(dic)
            else:
                prev_income= float(df_income["netIncome"][i+1])
                curr_income = float(df_income["netIncome"][i])
                if prev_income!=0.0:
                    growth_percent = ((curr_income-prev_income)/prev_income)*100
                    growth = (curr_income-prev_income)/prev_income
                    
                    date = df_income["date"][index]
                    dic = {"Date":str(date),"Earning_Growth_Percant":growth_percent,"Earning_Growth":growth}
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
                    dic = {"Date":str(date),"freeCashFlow_Growth_Percant":growth_percent, "freeCashFlow_Growth":growth}
                    fcf_growth_dict.append(dic)
            else:
                prev_fcf = float(df_cashflow["freeCashFlow"][i+1])
                curr_fcf = float(df_cashflow["freeCashFlow"][i])
                if prev_fcf !=0.0:
                    growth_percent = ((curr_fcf-prev_fcf)/prev_fcf)*100
                    growth = (curr_fcf-prev_fcf)/prev_fcf
                    
                    date = df_cashflow["date"][index]
                    dic = {"Date":str(date),"freeCashFlow_Growth_Percant":growth_percent, "freeCashFlow_Growth":growth}
                    fcf_growth_dict.append(dic)
            i+=1
        return fcf_growth_dict
    
    
    def netProfit_margin_growth(self, symbol_name):
        netProfit_growth_dict = []
        df_income,_ = self.obj.getIncomeStatements(symbol_name)
        i=0
        df_length = len(df_income)-1
        for index in range(df_length+1):          
            if i==df_length:
                if df_income["revenue"][index]!=0:
                    net_income = float(df_income["netIncome"][index])
                    revenue = float(df_income["revenue"][index])
                    growth_percent = (net_income/revenue)*100
                    growth = net_income/revenue
                    
                    date = df_income["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"netProfit_Growth_Percant":growth_percent, "netProfit_Growth":growth}
                    netProfit_growth_dict.append(dic)
            else:
                net_income = float(df_income["netIncome"][i+1])
                revenue = float(df_income["revenue"][i])
                if revenue !=0.0:
                    growth_percent = (net_income/revenue)*100
                    growth = net_income/revenue
                    
                    date = df_income["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"netProfit_Growth_Percant":growth_percent, "netProfit_Growth":growth}
                    netProfit_growth_dict.append(dic)
            i+=1
        return netProfit_growth_dict
    
    
    def operating_margin_growth(self, symbol_name):
        operating_growth_dict = []
        df_income,_ = self.obj.getIncomeStatements(symbol_name)
        i=0
        df_length = len(df_income)-1
        for index in range(df_length+1):          
            if i==df_length:
                if df_income["revenue"][index]!=0:
                    operating_income = float(df_income["operatingIncome"][index])
                    revenue = float(df_income["revenue"][index])
                    growth_percent = (operating_income/revenue)*100
                    growth = operating_income/revenue
                    
                    date = df_income["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"operatingIncome_Growth_Percant":growth_percent, "operatingProfit_Growth":growth}
                    operating_growth_dict.append(dic)
            else:
                operating_income = float(df_income["operatingIncome"][i+1])
                revenue = float(df_income["revenue"][i])
                if revenue !=0.0:
                    growth_percent = (operating_income/revenue)*100
                    growth = operating_income/revenue
                    
                    date = df_income["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"operatingIncome_Growth_Percant":growth_percent, "operatingProfit_Growth":growth}
                    operating_growth_dict.append(dic)
            i+=1
        return operating_growth_dict
    
    def gross_margin_growth(self, symbol_name):
        gross_growth_dict = []
        df_income,_ = self.obj.getIncomeStatements(symbol_name)
        i=0
        df_length = len(df_income)-1
        for index in range(df_length+1):          
            if i==df_length:
                if df_income["revenue"][index]!=0:
                    gross_profit= float(df_income["grossProfit"][index])
                    revenue = float(df_income["revenue"][index])
                    growth_percent = (gross_profit/revenue)*100
                    growth = gross_profit/revenue
                    
                    date = df_income["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"grossProfit_Growth_Percant":growth_percent, "operatingIncome_Growth":growth}
                    gross_growth_dict.append(dic)
            else:
                gross_profit = float(df_income["grossProfit"][i+1])
                revenue = float(df_income["revenue"][i])
                if revenue !=0.0:
                    growth_percent = (gross_profit/revenue)*100
                    growth = gross_profit/revenue
                    
                    date = df_income["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"grossProfit_Growth_Percant":growth_percent, "grossProfit_Growth":growth}
                    gross_growth_dict.append(dic)
            i+=1
        return gross_growth_dict
    
    
    def eps_margin_growth(self, symbol_name):
        eps_growth_dict = []
        df_income,_ = self.obj.getIncomeStatements(symbol_name)
        i=0
        df_length = len(df_income)-1
        for index in range(df_length+1):          
            if i==df_length:
                if df_income["eps"][index]!=0:
                    prev_eps = float(df_income["eps"][index])
                    curr_eps = float(df_income["eps"][index])
                    growth_percent = ((curr_eps-prev_eps)/prev_eps)*100
                    growth = (curr_eps-prev_eps)/prev_eps
                    
                    date = df_income["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"eps_Growth_Percant":growth_percent, "eps_Growth":growth}
                    eps_growth_dict.append(dic)
            else:
                prev_eps = float(df_income["eps"][i+1])
                curr_eps = float(df_income["eps"][i])
                if prev_eps !=0.0:
                    growth_percent = ((curr_eps-prev_eps)/prev_eps)*100
                    growth = (curr_eps-prev_eps)/prev_eps
                    
                    date = df_income["date"][index]
                    dic = {"Symbol":symbol_name,"Date":str(date),"eps_Growth_Percant":growth_percent, "eps_Growth":growth}
                    eps_growth_dict.append(dic)
            i+=1
        return eps_growth_dict
    '''
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
                    dic = {"Date":str(date),"MarketSize_Growth_Percant":growth_percent,"MarketSize_Growth":growth}
                    ms_growth_dict.append(dic)
            else:
                prev_ms = float(df_balance["totalStockholdersEquity"][i+1])
                curr_ms = float(df_balance["totalStockholdersEquity"][i])
                if prev_ms!=0.0:
                    growth_percent = ((curr_ms-prev_ms)/prev_ms)*100
                    growth = (curr_ms-prev_ms)/prev_ms
                    
                    
                    date = df_balance["date"][index]
                    dic = {"Date":str(date),"MarketSize_Growth_Percant":growth_percent,"MarketSize_Growth":growth}
                    ms_growth_dict.append(dic)
            i+=1
        return ms_growth_dict
    '''
        
                
    
    
#rev_growth = Find_Growth().revenue_growth("AAPL")

#earning_growth = Find_Growth_Quarter().earning_growth("AAPL")
'''
netProfit = Find_Growth_Quarter().netProfit_margin_growth("AAPL")
operatingProfit = Find_Growth_Quarter().operating_margin_growth("AAPL")
grossProfit = Find_Growth_Quarter().gross_margin_growth("AAPL")
epsProfit = Find_Growth_Quarter().eps_margin_growth("AAPL")
'''
'''
fcf_growth = Find_Revenue().fcf_growth("AAPL")
ms_growth = Find_Revenue().marketSize_growth("AAPL")'''