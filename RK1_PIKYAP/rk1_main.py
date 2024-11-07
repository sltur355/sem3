class Razdel:
    def __init__(self, id_razdela, name):
        self.id_razdela = id_razdela  # Идентификатор раздела
        self.name = name  # Название раздела
        self.documents = []  # Список документов в разделе

    def add_document(self, document):
        self.documents.append(document)  # Добавление документа в раздел


class Dokument:
    def __init__(self, id_dokumenta, name, salary):
        self.id_dokumenta = id_dokumenta  # Идентификатор документа
        self.name = name  # Название документа
        self.salary = salary  # Признак, связанный с документом (зарплата)


# Создание разделов
razdel1 = Razdel(1, "Анализ")
razdel2 = Razdel(2, "Бухгалтерия")
razdel3 = Razdel(3, "Маркетинг")

# Создание документов
dokument1 = Dokument(1, "Отчет по продажам", 50000)
dokument2 = Dokument(2, "Финансовый отчет", 60000)
dokument3 = Dokument(3, "Анализ рынка", 70000)
dokument4 = Dokument(4, "План продаж", 55000)

# Добавление документов в разделы
razdel1.add_document(dokument3)
razdel1.add_document(dokument1)
razdel2.add_document(dokument2)
razdel3.add_document(dokument4)

# Список всех разделов
razdely = [razdel1, razdel2, razdel3]

# Запрос 1: Вывести список всех разделов, у которых название начинается с буквы «А», и список документов в них.
razdely_s_A = [
    (razdel.name, [document.name for document in razdel.documents])
    for razdel in razdely if razdel.name.startswith("А")
]

print("Разделы с названием на 'А' и их документы:")
for name, documents in razdely_s_A:
    print(f"Раздел: {name}, Документы: {', '.join(documents)}")

# Запрос 2: Вывести список отделов с максимальной зарплатой документов в каждом отделе, отсортированный по максимальной зарплате.
max_salary = [
    (razdel.name, max(document.salary for document in razdel.documents))
    for razdel in razdely
]

max_salary.sort(key=lambda x: x[1], reverse=True)  # Сортировка по убыванию

print("Разделы с максимальной зарплатой документов:")
for name, salary in max_salary:
    print(f"Раздел: {name}, Максимальная зарплата: {salary}")

# Запрос 3: Вывести список всех связанных документов и разделов, отсортированный по разделам.
svyazannye_dannye = [
    (razdel.name, document.name)
    for razdel in razdely for document in razdel.documents
]

svyazannye_dannye.sort(key=lambda x: x[0])  # Сортировка по названиям разделов

print("Связанные документы и разделы:")
for razdel, dokument in svyazannye_dannye:
    print(f"Раздел: {razdel}, Документ: {dokument}")
