def insertInToMid(lst, num, str):
    """
    Функция для вставки строки в середину списка.
    
     lst -- список строк
    str -- строка для вставки
    """
    mid_index = len(lst) // 2
    lst.insert(mid_index, num, str)    "добавил нам"
    return lst



"""
CКРЫТО НА ВЕТКЕ dev

def insertAtPosition(lst, position, num, str):
    
    Функция для вставки строки в указанную позицию списка
    lst -- список строк
    position -- позиция для вставки строки
    num -- число для проверки возможности вставки
    str -- строка для вставки

    if position <= len(lst):
        lst.insert(position, str)
        return lst
    else:
        return "operation is not possible" 

"""