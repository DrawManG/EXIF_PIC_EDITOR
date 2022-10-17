"""
Класс: 
    - Взять даты и мена
    - Добавить в словарь {name:data}
    - Сортировать по дате
    - Возвращать в массивах новые даты и имена

Ексель:
    - Н столбец = "А-Я" сортировка

Интерфейс:
    -checkbox = "A-Я"

Код: 
    - Объеденение всего
"""
from datetime import datetime

class sort_az():
    
    def join(name,data):
        data = sort_az.datatime_convert(data)
        dictionary = sort_az.create_dictionary(name,data)
        sorted_dictionary = sort_az.sort_AZ(dictionary)

        print(dictionary)
        
    def datatime_convert(_data):
        _ = []
        for dat in range(len(_data)):
            _.append(datetime.strptime(_data[dat].replace(".","-") , '%d-%m-%Y %H:%M:%S'))
        return _
    def create_dictionary(name,data):
        _base = {}
        for i in range(len(name)):
            _base[name[i]] = data[i]
        return _base
    
    def sort_AZ(dictionary):
        _base = {}

        return _base





sort_az.join(name=['1','2','3'],data=["19.04.2020 14:32:00","19.05.2020 14:12:40","24.04.2022 14:32:00"])