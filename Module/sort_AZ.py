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

class sort_az():
    
    def join(name,data):
        dictionary = sort_az.create_dictionary(name,data)
        print(dictionary)
        
    
    def create_dictionary(name,data):
        _base = {}
        for i in range(len(name)):
            _base[name[i]] = data[i]
        return _base




sort_az.join(name=['1','2','3'],data=["19.04.2020 14:32:00","19.05.2020 14:12:40","24.04.2022 14:32:00"])