import urllib.request
import pandas as pd
import json
class Accounting_Info_Quarter:

    def __init__(self):
        pass
        
    def getSymbols(self):
        df_symbol = pd.read_csv("symbol&Companies.csv")
        symbol_list = df_symbol["SymName"].to_list()
        return symbol_list

    def getIncomeStatements(self,symbol_name):
        url_incomeStatement= "https://financialmodelingprep.com/api/v3/income-statement/"+symbol_name+"?period=quarter&limit=120&apikey="+"2b2bbacbc149bcba58903f591ae3d3c8"
        source_incomeStatement =  urllib.request.urlopen(url_incomeStatement).read()
        list_of_incomeStatement = json.loads(source_incomeStatement)
        df_income = pd.DataFrame(list_of_incomeStatement)
        return df_income, list_of_incomeStatement
    
    def getAnnualBalanceSheet(self, symbol_name):
        url_balanceSheet = "https://financialmodelingprep.com/api/v3/balance-sheet-statement/"+symbol_name+"?period=quarter&limit=120&apikey="+"2b2bbacbc149bcba58903f591ae3d3c8"
        source_balanceSheet = urllib.request.urlopen(url_balanceSheet).read()
        list_of_balanceSheet =  json.loads(source_balanceSheet)
        df_balance= pd.DataFrame(list_of_balanceSheet)
        return df_balance, list_of_balanceSheet
    
    def getAnnualCashFlow(self,symbol_name):
        url_cash_flow = "https://financialmodelingprep.com/api/v3/cash-flow-statement/"+symbol_name+"?period=quarter&limit=120&apikey="+"2b2bbacbc149bcba58903f591ae3d3c8"
        source_cashFlow = urllib.request.urlopen(url_cash_flow).read()
        list_of_cashFlow =  json.loads(source_cashFlow)
        df_cashflow = pd.DataFrame(list_of_cashFlow)
        return df_cashflow, list_of_cashFlow
    
    def getEV(self, symbol_name):
        url_ev = "https://financialmodelingprep.com/api/v3/enterprise-values/"+symbol_name+"?period=quarter&limit=120&apikey="+"2b2bbacbc149bcba58903f591ae3d3c8"
        source_ev = urllib.request.urlopen(url_ev).read()
        list_of_ev =  json.loads(source_ev)
        df_ev = pd.DataFrame(list_of_ev)
        return df_ev,list_of_ev
    

    
'''
income_statement_df , income_statement_list = Accounting_Info().getIncomeStatements("AAPL")
balance_sheet_df, balance_sheet_list = Accounting_Info().getAnnualBalanceSheet("AAPL")
cash_flow_df , cash_flow_list = Accounting_Info().getAnnualCashFlow("AAPL")
ev_df , ev_list = Accounting_Info().getEV("AAPL")
#symbols = Accounting_Info().getSymbols()
'''