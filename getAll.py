from find_growth import Find_Growth
from find_multiple import Find_Multiple

class Result:
    
    def __init__(self):
        self.fg = Find_Growth()
        self.fm = Find_Multiple()
        pass
    
    def result(self,symbol_name):
        result_dict = {}
        multiple_revenue_dict,state_multiple_revenue = self.fm.multiple_of_Revenue(symbol_name)
        multiple_fcf_dict,state_multiple_fcf = self.fm.multiple_of_FCF(symbol_name)
        multiple_ebitda_dict,state_multiple_ebitda = self.fm.multiple_of_EBITDA(symbol_name)
        multiple_gmv_dict,state_multiple_gmv = self.fm.multiple_of_GMV(symbol_name)
        rank_star = 0
        states = [state_multiple_revenue["value"], state_multiple_fcf["value"],
                  state_multiple_ebitda["value"],state_multiple_gmv["value"]]
        for state in states:
            if state=="UnderValued":
                rank_star+=1
        
        revenue_growth= self.fg.revenue_growth(symbol_name)
        fcf_growth = self.fg.fcf_growth(symbol_name)
        ms_growth = self.fg.marketSize_growth(symbol_name)
        earn_growth = self.fg.earning_growth(symbol_name)
        print("Symbol name:"+symbol_name)
        print("Multiple of Revenue: "+)
        return rank_star, state_multiple_revenue,state_multiple_fcf,state_multiple_ebitda, state_multiple_gmv,revenue_growth,fcf_growth,ms_growth,earn_growth
    
    
#states = Result().result("AAPL")
        
        