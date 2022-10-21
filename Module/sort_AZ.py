"""
Класс: 
    - Взять даты и мена                         +
    - Добавить в словарь {name:data}            +   
    - Сортировать по дате                       +  
    - Возвращать в массивах новые даты и имена +

Ексель:
    - Н столбец = "А-Я" сортировка +

Интерфейс:
    -checkbox = "A-Я" +

Код: 
    - Объеденение всего
"""
from datetime import datetime

class sort_az():
    
    def join(name,data):
        data = sort_az.datatime_convert(data)
        dictionary = sort_az.create_dictionary(name,data)
        sorted_dictionary = sort_az.sort_AZ(dictionary)
        key,value = sort_az.dict_convert_to_massive(sorted_dictionary)
        print("key",key)
        print("value",value)
        return key,value
        
    def dict_convert_to_massive(_sorted):
        key = list(_sorted.keys())
        value = list(_sorted.values())
        
        return key,value

    def datatime_convert(_data):
        _ = []
        for dat in range(len(_data)):
            _.append(datetime.strptime(_data[dat].replace(".","-") , '%Y-%m-%d %H:%M:%S'))
        return _
    def create_dictionary(name,data):
        _base = {}
        for i in range(len(name)):
            _base[name[i]] = data[i]
        return _base
    
    def sort_AZ(dictionary):
        sorted_values = sorted(dictionary.values()) 
        sorted_dict = {}

        for i in sorted_values:
            for k in dictionary.keys():
                if dictionary[k] == i:
                    sorted_dict[k] = dictionary[k]
                    break
        

        return sorted_dict



"""
DEBUG COMMAND:
    #sort_az.join(name=['1','2','3'],data=["19.04.2024 14:32:00","19.05.2020 14:12:40","24.04.2022 14:32:00"])
    and print def -join-
"""
sort_az.join(name=['1','2','3'],data=['2022.10.07 09:55:16', '2022.10.07 10:55:41', '2022.10.07 12:30:14'])