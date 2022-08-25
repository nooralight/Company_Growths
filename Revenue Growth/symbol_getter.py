import transactionsBT as bt


class Symbol:
    
    def __init__(self):
        pass
    
    
    def getSymandCompName(self):
        query1 = "SELECT SymName,ComName FROM tblSymbol WHERE SymName NOT LIKE '^%'"
        df_sp_symbols = bt.fncGetDataAsPanda(query1)
        #df_sp_symbols.to_csv("symbol&Companies.csv")
        return df_sp_symbols()
        
    
    
Symbol().getSymandCompName()