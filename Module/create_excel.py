import pandas as pd
import os
from openpyxl import Workbook , load_workbook
class create_excel:
    
    def create_excel(self,Name,Data,folder,type_sheet,name_pth):
        print('name pth', name_pth)
        from datetime import datetime
        import xlwt
        workbook = xlwt.Workbook('1.xls')
        worksheet = workbook.add_sheet(type_sheet,cell_overwrite_ok=True)
        worksheet5 = workbook.add_sheet("New name") 
        if not name_pth == "*":

            i = 0 
            print(len(Name),len(Data),len(folder),len(type_sheet),len(name_pth))
            while i < len(name_pth):
                print(i,"из ",len(name_pth))
                worksheet.write(i,1, str(Name[i]))
                worksheet.write(i,7, str(Data[i]))
                
                worksheet5.write(i,1, str(name_pth[i]))
                worksheet5.write(i,7, str(Data[i]))
                i+=1

        else:
            
                i = 0 
                while i < len(Name):
                    worksheet.write(i,1, str(Name[i]))
                    worksheet.write(i,7, str(Data[i]))
                
                i+=1


        
        workbook.save(folder+str(datetime.now()).replace(":","_").replace(" ","-").replace(".","_")+".xls" )
