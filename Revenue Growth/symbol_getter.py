import transactionsBT as bt
import pandas as pd
import re
#line = re.sub('[!@#$]', '', line)

class Symbol:
    
    def __init__(self):
        pass
    
    
    def getSymandCompName(self):
        query1 = "SELECT SymName,ComName FROM tblSymbol WHERE SymName NOT LIKE '^%'"
        df_sp_symbols = bt.fncGetDataAsPanda(query1)
        #df_sp_symbols.to_csv("symbol&Companies.csv")
        return df_sp_symbols
        
    def writeCSVofCompany(self):
        query = "SELECT SymName,ComName FROM tblSymbol WHERE SymName NOT LIKE '^%'"
        df_sp_symbols = bt.fncGetDataAsPanda(query)
        df_sp_symbols.to_csv("symbol&Companies.csv")

    
Symbol().writeCSVofCompany()