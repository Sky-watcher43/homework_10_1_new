def filter_by_state(my_list: list[dict], state='EXECUTED') -> list[dict]:
    ''' Принимает список словарей и возвращает новый список словарей
    со словарями. у которых ключ соответствует заданному значению'''
    new_list = []
    for elem in my_list:
        if elem.get("state") == state:
            new_list.append(elem)
    return new_list


result = filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
print(result)


def sort_by_date(date_list: list[dict], reverse=True) -> list[dict]:
    '''Принимает список словарей и возвращает новый список, отсортированный по дате'''
    new_date = sorted(date_list, reverse=reverse, key=lambda x: x.get("date"))
    return new_date


result = sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
print(result)
