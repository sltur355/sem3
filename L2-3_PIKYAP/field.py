def field(items, *args):
    assert len(args) > 0  # переданы хотя бы одни аргументы

    for item in items:
        if len(args) == 1:  # если передан только один аргумент
            value = item.get(args[0])
            if value is not None:
                yield value  # выдаем значение, если оно не None
        else:  # если передано несколько аргументов
            result = {arg: item.get(arg) for arg in args if item.get(arg) is not None}
            if result:  # если в результате есть хотя бы одно значение
                yield result  # выдаем словарь с непустыми значениями

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стул', 'price': None, 'color': 'white'},
    {'title': None, 'price': None, 'color': 'blue'}]

# тестирование
print(list(field(goods, 'title')))  # ['Ковер', 'Диван для отдыха', 'Стул']
print(list(field(goods, 'title', 'price')))  # [{'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}]