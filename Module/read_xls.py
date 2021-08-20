import random
import string
import xlrd

class read_xls:
 def read_xls(path, sheet_name):
    def data_format(data):
        date, time = str(data).split(" ")
        return date.replace("-", ".") + " " + time[:-2] + str(random.choice(string.digits[:6])) + \
               str(random.choice(string.digits))
    
    rb = xlrd.open_workbook(path)
    sheet = rb.sheet_by_name(sheet_name)
    names = []
    dates = []

    for i in range(5, sheet.nrows):
        names.append(sheet.cell_value(rowx=i, colx=1))
        date = str(xlrd.xldate_as_datetime(sheet.cell_value(rowx=i, colx=7), rb.datemode))
        dates.append(data_format(date))
    

    return names, dates

