import json
from datetime import datetime
from config import operations_path


def last_five_operations():
    '''Функция возвращяет список пяти последних успешных операций'''

    # открываем файл и читаем содержимое, получаем строку из json
    with open(operations_path, encoding='utf-8') as f:
        data = f.read()

    # получаем список словарей операций для обработки
    transact_list = json.loads(data)

    # формируем список с успешными транзакциями
    executed_list = []
    for operation in transact_list:
        if operation.get('state', False) != False and operation['state'] == 'EXECUTED':
            executed_list.append(operation)


    # выявляем даты последних успешных 5-ти операций
    valid_dates = []
    for i in executed_list:
        valid_dates.append(i['date'])
    valid_dates.sort()
    last_5_dates = valid_dates[-1:-6:-1]


    # формируем список валидных словарей из пяти последних операций
    valid_list = []
    for j in last_5_dates:
        for i in executed_list:
            if i['date'] == j:
                valid_list.append(i)

    return valid_list


def result_description(dict_):
    '''Фунция возвращает строку с датой и описанием в формате согласно ТЗ'''
    d = datetime.strptime(dict_['date'][:10], "%Y-%m-%d") # преобразуем строку в объект datetime
    return f"{d.strftime('%d.%m.%Y')} {dict_['description']}"


def hide_number(number):
    '''функция маскирует номер счета или карты'''
    if len(number) == 16:
        return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    else:
        return f"**{number[-4:]}"


def result_transaction(dict_):
    '''Фукция возвращает путь транзакции'''
    bell_to = dict_['to'].split()
    if dict_.get('from', False) != False:
        bell_from = dict_['from'].split()
        return f"{' '.join(bell_from[:-1])} {hide_number(bell_from[-1])} -> {' '.join(bell_to[:-1])} {hide_number(bell_to[-1])}"
    else:
        return f"{' '.join(bell_to[:-1])} {hide_number(bell_to[-1])}"


def result_summ(dict_):
    '''Фунция возвращает строку с суммой транзакции'''
    return f"{dict_['operationAmount']['amount']} {dict_['operationAmount']['currency']['name']}"

