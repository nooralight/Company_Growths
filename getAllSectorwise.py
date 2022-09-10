from subsector_marketsize_Annual import Subsector_Growth_Annual
from find_growth_Annual import Find_Growth_Annual

from subsector_marketsize_Quarter import Subsector_Growth_Quarter
from find_growth_Quarter import Find_Growth_Quarter
import pandas as pd


'''
    We will rank the companies in 3 levels.
     - First Division : higher than mean in subsector
     - Second Division : Lower than mean in subsector
     
'''
class Show:
    
    def __init__(self):
        self.subsector_marketsize_Annual = Subsector_Growth_Annual()
        self.find_growth = Find_Growth_Annual()
        
        self.subsector_marketsize_Quarter = Subsector_Growth_Quarter()
        self.find_growth_Quarter = Find_Growth_Quarter()
        
        
        self.symbols,self.sub_sectors = self.symbol_getter()

    def symbol_getter(self):
        _,symbol_pd = Subsector_Growth_Annual().getting_subsectors()
        symbols = symbol_pd["symbol"].tolist()
        sub_sectors = symbol_pd["subSector"].tolist()
        return symbols, sub_sectors

    def showing_result_annual(self):
        result_dictionary_annual= []
        #print(type(self.symbols))
        for i in range(len(self.symbols)//75):
            revenue_dict = self.find_growth.revenue_growth(self.symbols[i])
            earning_dict = self.find_growth.earning_growth(self.symbols[i])
            fcf_dict = self.find_growth.fcf_growth(self.symbols[i])
            #ms_dict = self.find_growth.marketSize_growth(self.symbols[i])
            
            symbol_name = self.symbols[i]
            date = revenue_dict[0]["Date"]
            #print(self.symbols[i], revenue_dict[i]["Date"],revenue_dict[i]["Revenue_Growth_Percant"],self.subsector_marketsize.subsector_wise_revGrowth(self.symbols[i]))
            individual_growth_rate_revenue = revenue_dict[0]["Revenue_Growth_Percant"]
            subsector_growth_rate_revenue, state_revenue = self.subsector_marketsize_Annual.subsector_wise_revGrowth(self.symbols[i])
            individual_growth_rate_earning= earning_dict[0]["Earning_Growth_Percant"]
            subsector_growth_rate_earning, state_earning =  self.subsector_marketsize_Annual.subsector_wise_earnGrowth(self.symbols[i])
            individual_growth_rate_fcf = fcf_dict[0]["freeCashFlow_Growth_Percant"]
            subsector_growth_rate_fcf, state_fcf = self.subsector_marketsize_Annual.subsector_wise_fcfGrowth(self.symbols[i])
            #individual_growth_rate_ms = ms_dict[0]["MarketSize_Growth_Percant"]
            #subsector_growth_rate_ms, state_ms = self.subsector_marketsize_Annual.subsector_wise_msGrowth(self.symbols[i])
            
            temp_dict = {"symbol_name":symbol_name, "date":date, "individual_growth_rate_revenue (%)":individual_growth_rate_revenue,
                         "individual_growth_rate_earning (%)":individual_growth_rate_earning,"individual_growth_rate_fcf (%)":individual_growth_rate_fcf,
                         "subsector_growth_rate_revenue (%)":subsector_growth_rate_revenue,
                         "RateRevenue_Growth":state_revenue,"subsector_growth_rate_earning (%)":subsector_growth_rate_earning,
                         "RateEarning_Growth":state_earning,"subsector_growth_rate_fcf (%)":subsector_growth_rate_fcf,
                         "RateFCF_Growth":state_fcf}
            #"individual_growth_rate_ms (%)":individual_growth_rate_ms,,"subsector_growth_rate_ms (%)":subsector_growth_rate_ms,"RateMarketSize_Growth":state_ms
            result_dictionary_annual.append(temp_dict)
            print(i+1, "th process finished. ",(len(self.symbols)//75)-(i+1)," preocesses remaining..")
        df_result = pd.DataFrame(result_dictionary_annual)
        return df_result
    
    def showing_result_Quarter(self):
        result_dictionary_Quarter= []
        #print(type(self.symbols))
        for i in range(len(self.symbols)//75):
            revenue_dict = self.find_growth_Quarter.revenue_growth(self.symbols[i])
            earning_dict = self.find_growth_Quarter.earning_growth(self.symbols[i])
            fcf_dict = self.find_growth_Quarter.fcf_growth(self.symbols[i])
            ms_dict = self.find_growth_Quarter.marketSize_growth(self.symbols[i])
            
            symbol_name = self.symbols[i]
            date = revenue_dict[0]["Date"]
            #print(self.symbols[i], revenue_dict[i]["Date"],revenue_dict[i]["Revenue_Growth_Percant"],self.subsector_marketsize.subsector_wise_revGrowth(self.symbols[i]))
            individual_growth_rate_revenue = revenue_dict[0]["Revenue_Growth_Percant"]
            subsector_growth_rate_revenue, state_revenue = self.subsector_marketsize_Quarter.subsector_wise_revGrowth(self.symbols[i])
            individual_growth_rate_earning= earning_dict[0]["Earning_Growth_Percant"]
            subsector_growth_rate_earning, state_earning =  self.subsector_marketsize_Quarter.subsector_wise_earnGrowth(self.symbols[i])
            individual_growth_rate_fcf = fcf_dict[0]["freeCashFlow_Growth_Percant"]
            subsector_growth_rate_fcf, state_fcf = self.subsector_marketsize_Quarter.subsector_wise_fcfGrowth(self.symbols[i])
            individual_growth_rate_ms = ms_dict[0]["MarketSize_Growth_Percant"]
            subsector_growth_rate_ms, state_ms = self.subsector_marketsize_Quarter.subsector_wise_msGrowth(self.symbols[i])
            
            temp_dict = {"symbol_name":symbol_name, "date":date, "individual_growth_rate_revenue (%)":individual_growth_rate_revenue,
                         "individual_growth_rate_earning (%)":individual_growth_rate_earning,"individual_growth_rate_fcf (%)":individual_growth_rate_fcf,
                         "individual_growth_rate_ms (%)":individual_growth_rate_ms,"subsector_growth_rate_revenue (%)":subsector_growth_rate_revenue,
                         "RateRevenue_Growth":state_revenue,"subsector_growth_rate_earning (%)":subsector_growth_rate_earning,
                         "RateEarning_Growth":state_earning,"subsector_growth_rate_fcf (%)":subsector_growth_rate_fcf,
                         "RateFCF_Growth":state_fcf,"subsector_growth_rate_ms (%)":subsector_growth_rate_ms,"RateMarketSize_Growth":state_ms}
            result_dictionary_Quarter.append(temp_dict)
            print(i+1, "th process finished. ",(len(self.symbols)//75)-(i+1)," preocesses remaining..")
        df_result = pd.DataFrame(result_dictionary_Quarter)
        return df_result
#print("Annual Report....")
#annual_result = Show().showing_result_annual()
#print()
print("Quarterly Report....")
quarter_result = Show().showing_result_Quarter()

#margin growth




'''
sector, kist = Subsector_Growth().getting_subsectors()
for index, row in kist.iterrows():
    print(row["symbol"])
'''
'''

symbol_name, date,individual_growth_rate_revenue, subsector_growth_rate_revenue =symbol, revenue_dict["Date"],revenue_dict["Revenue_Growth_Percant"],self.subsector_marketsize.subsector_wise_revGrowth(symbol)  
print("Symbol = ",symbol_name," ,date= ",date," ,Company Growth= ",individual_growth_rate_revenue,"% ,SubsectorWise Growth= ",subsector_growth_rate_revenue,"%")

'''