import pandas as pd
import transactionsBT as bt


class Revenue_growth:
    def  __init__(self):
        pass
    
    def gettingInfo(self):
        query1 = "select SymName, revenue,costOfRevenue,dtDate as Date_X from tblAnnualIncomeStatment"
        df = bt.fncGetDataAsPanda(query1)
        #df.to_csv("revenue_info_company.csv")
        return df
    def revenue_growth_by_cogs(self):
        query2 = "select SymName, revenue/costOfRevenue as ['MultipleOfRevenue'],dtDate as Date_X  from tblAnnualIncomeStatment where NOT costOfRevenue=0 order by SymName"
        df = bt.fncGetDataAsPanda(query2)
        #print(df)
        return df
    
    def company_growth(self):
        symbols = self.gettingInfo()['SymName'].to_list()
        symbols = sorted(list(set(symbols)))
        company_growth_individual = []
        for symbol in symbols:
            query = "select SymName, revenue/costOfRevenue as ['MultipleOfRevenue'],dtDate as Date_X  from tblAnnualIncomeStatment where SymName='"+symbol+"'and NOT costOfRevenue=0 order by dtDate"
            df = bt.fncGetDataAsPanda(query)
            company_growth_individual.append(df)
        return company_growth_individual
revenue_based_on_cogs = Revenue_growth().revenue_growth_by_cogs()

individual_reports = Revenue_growth().company_growth()



