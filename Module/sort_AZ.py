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
    
    def join(name,data,path):
        #Добавление даты из стринг в дататайм
        data = sort_az.datatime_convert(data)
        #Добавить в словарь все массивы
        dictionary = sort_az.create_dictionary(name,data,path)
        #отсортировать массивы по дате в взначении словаря [1]
        sorted_dictionary = sort_az.sort_AZ(dictionary)
        #Вывод обратно по массивам
        key,value,path = sort_az.dict_convert_to_massive(sorted_dictionary)

        return key,value,path
        
    def dict_convert_to_massive(_sorted):
        key = list(_sorted.keys())
        values = list(_sorted.values())
        value = []
        path = []
        for i in range(len(key)):
            value.append(values[i][0])
            path.append(values[i][1])

        return key,value,path

    def datatime_convert(_data):
        _ = []
        for dat in range(len(_data)):
            _.append(datetime.strptime(_data[dat].replace(".","-") , '%Y-%m-%d %H:%M:%S'))
        return _
    def create_dictionary(name,data,path):
        _base = {}
        for i in range(len(name)):
            _base[name[i]] = data[i],path[i]
        print("_base",_base)
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
#sort_az.join(name=['1','2','3'],data=['2022.10.07 09:55:16', '2024.10.07 10:55:41', '2022.10.07 12:30:14'],path=['c:\\фото — копия\\1.JPG', 'c:\\фото — копия\\2.JPG', 'c:\\фото — копия\\3.JPG'])