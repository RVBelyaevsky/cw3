import json
import os


def last_five_operations():
    # открываем файл и читаем содержимое, получаем строку из json
    with open(os.path.join("operations.json"), encoding='utf-8') as f:
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

