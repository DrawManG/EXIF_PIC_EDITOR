import pandas as pd
import os
from openpyxl import Workbook , load_workbook
class create_excel:
    
    def create_excel(self,Name,Data,folder,type_sheet):
        
        from datetime import datetime
        import xlwt
        workbook = xlwt.Workbook('1.xls')
        worksheet = workbook.add_sheet(type_sheet,cell_overwrite_ok=True) 
        
        i = 0 
        while i < len(Name):
            worksheet.write(i,1, str(Name[i]))
            worksheet.write(i,7, str(Data[i]))
            i+=1
        
        workbook.save(folder+str(datetime.now()).replace(":","_").replace(" ","-").replace(".","_")+".xls" )
