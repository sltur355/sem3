# unique.py

class Unique:
    def __init__(self, items, **kwargs):  #конструктор, принимает список или генератор
        self.items = items
        self.ignore_case = kwargs.get('ignore_case', False) #флаг, проверяет регистр
        self.seen = set()   #пустое множество для отслеживания встреченнных элементов
        self.iterator = iter(items)   #для последовательного извлечения элементов

    def __iter__(self): #метод - возвращает сам объект
        return self

    def __next__(self): #ищет следующий уникальный элемент
        while True:
            try:
                item = next(self.iterator)

                key = item.lower() if self.ignore_case and isinstance(item, str) else item

                # Проверяем, был ли элемент уже встречен
                if key not in self.seen:
                    self.seen.add(key)
                    return item
            except StopIteration:
                raise StopIteration


if __name__ == "__main__":
    from gen_random import gen_random

    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    unique_data1 = Unique(data1)
    print(list(unique_data1))  # [1, 2]

    data2 = gen_random(10, 1, 3)
    unique_data2 = Unique(data2)
    print(list(unique_data2))  # [1, 2, 3]

    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    unique_data3 = Unique(data3)
    print(list(unique_data3))  #  ['a', 'A', 'b', 'B']

    unique_data4 = Unique(data3, ignore_case=True)
    print(list(unique_data4))  # ['a', 'b']