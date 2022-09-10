import urllib.request
import pandas as pd
import json
from download_Annual import Accounting_Info_Annual as AI
from find_growth_Annual import Find_Growth_Annual as FG

class Subsector_Growth_Annual:    
    '''
        Constructor
    '''
    def __init__(self):
        
        self.obj = AI()
        self.fg = FG()
    
    '''
        In this function we returned the name of unique sub sectors 
        - Return type = list
    '''
    def getting_subsectors(self,url):
        url_subsectors= url
        source_subsectors =  urllib.request.urlopen(url_subsectors).read()
        list_of_incomeStatement = json.loads(source_subsectors)
        df = pd.DataFrame(list_of_incomeStatement)
        df_new = df.iloc[:,[0,1,3]]
        arr = df_new["subSector"].tolist()
        list_of_subsectors = list(set(arr))
        return list_of_subsectors, df_new
        #df_new = df.iloc[:, [0,1,3]]
        

    # total revenue growth of a sub sector
    def total_subsector_revenue(self,subSector_list):
        total_growth_revenue = 0.0
        mean_arr =[]
        for symbol in subSector_list:
            revenue_dict = self.fg.revenue_growth(symbol)
            revenue_growth = revenue_dict[0]["Revenue_Growth"]
            #print("Symbol = ",symbol,", Growth-rate = ", revenue_growth)
            mean_arr.append(revenue_growth)
            #print(type(revenue_growth))
            total_growth_revenue+=revenue_growth
        max_growth = max(mean_arr)
        min_growth = min(mean_arr)
        mean_growth = (min_growth+max_growth)/2
        return total_growth_revenue, mean_growth,max_growth,min_growth
    
    # total market growth of a sub sector
    def total_subsector_market(self,subSector_list):
        total_growth_market = 0.0
        mean_arr = []
        for symbol in subSector_list:
            market_dict = self.fg.marketSize_growth(symbol)
            market_growth = market_dict[0]["MarketSize_Growth"]
            mean_arr.append(market_growth)
            #print("Symbol = ",symbol,", Growth-rate = ", market_growth)
            #print(type(revenue_growth))
            total_growth_market+=market_growth
        max_growth = max(mean_arr)
        min_growth = min(mean_arr)
        mean_growth = (min_growth+max_growth)/2
        return total_growth_market, mean_growth, max_growth, min_growth
    
    # total fcf growth of a sub sector
    def total_subsector_earning(self,subSector_list):
        total_growth_earning = 0.0
        mean_arr= []
        for symbol in subSector_list:
            earning_dict = self.fg.earning_growth(symbol)
            earning_growth = earning_dict[0]["Earning_Growth"]
            #print("Symbol = ",symbol,", Growth-rate = ", earning_growth)
            mean_arr.append(earning_growth)
            #print(type(revenue_growth))
            total_growth_earning+=earning_growth
        max_growth = max(mean_arr)
        min_growth = min(mean_arr)
        mean_growth = (min_growth+max_growth)/2
        return total_growth_earning, mean_growth, max_growth, min_growth
    
    
    # total earning growth of a sub sector
    def total_subsector_fcf(self,subSector_list):
        total_growth_fcf = 0.0
        mean_arr= []
        for symbol in subSector_list:
            fcf_dict = self.fg.fcf_growth(symbol)
            fcf_growth = fcf_dict[0]["freeCashFlow_Growth"]
            #print("Symbol = ",symbol,", Growth-rate = ", fcf_growth)
            mean_arr.append(fcf_growth)
            #print(type(revenue_growth))
            total_growth_fcf+=fcf_growth
        max_growth = max(mean_arr)
        min_growth = min(mean_arr)
        mean_growth = (min_growth+max_growth)/2
        return total_growth_fcf, mean_growth, max_growth,min_growth
    

    # Sub Sector wise Revenue Growth percantage
    def subsector_wise_revGrowth(self,symbol_name):
        _,df_subsector = self.getting_subsectors()
        sub_sector=""
        #print("Getting the Subsector")
        for index, row in df_subsector.iterrows():
            if row["symbol"]==symbol_name:
                sub_sector = row["subSector"]
                break
        #print("Done")
        #print("*****")
        #print("Getting total revenue growth of that company's subsector")
        same_sector_company = []
        for index, row in df_subsector.iterrows():
            if row["subSector"]==sub_sector:
                same_sector_company.append(row["symbol"])
                
        total,mean_growth,max_growth,min_growth = self.total_subsector_revenue(same_sector_company)
        
        
        #this company's revenue growth
        revenue_dict = self.fg.revenue_growth(symbol_name)
        revenue_growth = revenue_dict[0]["Revenue_Growth"]
        state = ""
        if revenue_growth==max_growth:
            state = "highest"
        elif revenue_growth==mean_growth:
            state = "mean"
        elif revenue_growth==min_growth:
            state = "lowest"
        elif revenue_growth>mean_growth and revenue_growth<max_growth:
            state ="high"
        elif revenue_growth<mean_growth and revenue_growth>min_growth:
            state="low"
        
        subsector_wise_revPercant = (revenue_growth/total)*100
        
        return subsector_wise_revPercant, state
    
    
    #Sub sector wise market size growth percantage
    def subsector_wise_msGrowth(self,symbol_name):
        _,df_subsector = self.getting_subsectors()
        sub_sector=""

        for index, row in df_subsector.iterrows():
            if row["symbol"]==symbol_name:
                sub_sector = row["subSector"]
                break

        same_sector_company = []
        for index, row in df_subsector.iterrows():
            if row["subSector"]==sub_sector:
                same_sector_company.append(row["symbol"])
                
        total,mean_growth,max_growth,min_growth = self.total_subsector_market(same_sector_company)
        
        
        #this company's revenue growth
        ms_dict = self.fg.marketSize_growth(symbol_name)
        ms_growth = ms_dict[0]["MarketSize_Growth"]
        state = ""
        if ms_growth==max_growth:
            state = "highest"
        elif ms_growth==mean_growth:
            state = "mean"
        elif ms_growth==min_growth:
            state = "lowest"
        elif ms_growth>mean_growth and ms_growth<max_growth:
            state ="high"
        elif ms_growth<mean_growth and ms_growth>min_growth:
            state="low"
        subsector_wise_msPercant = (ms_growth/total)*100
        
        return subsector_wise_msPercant,state
    
    
    #Sub sector wise earning growth percantage
    def subsector_wise_earnGrowth(self,symbol_name):
        _,df_subsector = self.getting_subsectors()
        sub_sector=""

        for index, row in df_subsector.iterrows():
            if row["symbol"]==symbol_name:
                sub_sector = row["subSector"]
                break

        same_sector_company = []
        for index, row in df_subsector.iterrows():
            if row["subSector"]==sub_sector:
                same_sector_company.append(row["symbol"])
                
        total,mean_growth,max_growth,min_growth = self.total_subsector_earning(same_sector_company)
        
        
        #this company's revenue growth
        earning_dict = self.fg.earning_growth(symbol_name)
        earning_growth = earning_dict[0]["Earning_Growth"]
        state = ""
        if earning_growth==max_growth:
            state = "highest"
        elif earning_growth==mean_growth:
            state = "mean"
        elif earning_growth==min_growth:
            state = "lowest"
        elif earning_growth>mean_growth and earning_growth<max_growth:
            state ="high"
        elif earning_growth<mean_growth and earning_growth>min_growth:
            state="low"
        subsector_wise_earningPercant = (earning_growth/total)*100
        
        return subsector_wise_earningPercant, state
    
    
    #Sub sector wise free cash flow growth percantage
    def subsector_wise_fcfGrowth(self,symbol_name):
        _,df_subsector = self.getting_subsectors()
        sub_sector=""

        for index, row in df_subsector.iterrows():
            if row["symbol"]==symbol_name:
                sub_sector = row["subSector"]
                break

        same_sector_company = []
        for index, row in df_subsector.iterrows():
            if row["subSector"]==sub_sector:
                same_sector_company.append(row["symbol"])
                
        total,mean_growth,max_growth,min_growth = self.total_subsector_fcf(same_sector_company)
        
        
        #this company's revenue growth
        fcf_dict = self.fg.fcf_growth(symbol_name)
        fcf_growth = fcf_dict[0]["freeCashFlow_Growth"]
        state = ""
        if fcf_growth==max_growth:
            state = "highest"
        elif fcf_growth==mean_growth:
            state = "mean"
        elif fcf_growth==min_growth:
            state = "lowest"
        elif fcf_growth>mean_growth and fcf_growth<max_growth:
            state ="high"
        elif fcf_growth<mean_growth and fcf_growth>min_growth:
            state="low"
        subsector_wise_fcfPercant = (fcf_growth/total)*100
        
        return subsector_wise_fcfPercant, state
    
'''
revenue_perc = Subsector_Growth().subsector_wise_revGrowth("AAPL")
markerSize_perc = Subsector_Growth().subsector_wise_msGrowth("AAPL")
earning_perc = Subsector_Growth().subsector_wise_earnGrowth("AAPL")
fcf_perc = Subsector_Growth().subsector_wise_fcfGrowth("AAPL")
'''