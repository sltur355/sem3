import unittest
from operator import itemgetter

class Razdel:
    def __init__(self, id_razdela, name):
        self.id_razdela = id_razdela  # Идентификатор раздела
        self.name = name  # Название раздела
        self.documents = []  # Список документов в разделе

    def add_document(self, document):
        self.documents.append(document)  # Добавление документа в раздел

    def get_documents(self):
        return self.documents


class Dokument:
    def __init__(self, id_dokumenta, name, salary):
        self.id_dokumenta = id_dokumenta  # Идентификатор документа
        self.name = name  # Название документа
        self.salary = salary  # Признак, связанный с документом (зарплата)


class DocumentManager:
    def __init__(self):
        self.razdely = []

    def add_razdel(self, razdel):
        self.razdely.append(razdel)

    def get_razdely_with_name_starting_with(self, letter):
        return [
            (razdel.name, [document.name for document in razdel.get_documents()])
            for razdel in self.razdely if razdel.name.startswith(letter)
        ]

    def get_max_salary_per_razdel(self):
        max_salary = [
            (razdel.name, max((document.salary for document in razdel.get_documents()), default=0))

            for razdel in self.razdely
        ]
        max_salary.sort(key=lambda x: x[1], reverse=True)  # Сортировка по убыванию
        return max_salary

    def get_all_linked_data(self):
        linked_data = [
            (razdel.name, document.name)
            for razdel in self.razdely for document in razdel.get_documents()
        ]
        linked_data.sort(key=lambda x: x[0])  # Сортировка по названиям разделов
        return linked_data

class TestDocumentManager(unittest.TestCase):
    def setUp(self):
        self.manager = DocumentManager()

        # Создание разделов
        self.razdel1 = Razdel(1, "Анализ")
        self.razdel2 = Razdel(2, "Бухгалтерия")
        self.razdel3 = Razdel(3, "Маркетинг")

        self.manager.add_razdel(self.razdel1)
        self.manager.add_razdel(self.razdel2)
        self.manager.add_razdel(self.razdel3)
        self.dokument1 = Dokument(1, "Отчет по продажам", 50000)
        self.dokument2 = Dokument(2, "Финансовый отчет", 60000)
        self.dokument3 = Dokument(3, "Анализ рынка", 70000)
        self.dokument4 = Dokument(4, "План продаж", 55000)

        # Добавление документов в разделы
        self.razdel1.add_document(self.dokument3)
        self.razdel1.add_document(self.dokument1)
        self.razdel2.add_document(self.dokument2)
        self.razdel3.add_document(self.dokument4)

    def test_get_razdely_with_name_starting_with_A(self):
        result = self.manager.get_razdely_with_name_starting_with("А")
        expected = [("Анализ", ["Анализ рынка", "Отчет по продажам"])]
        self.assertEqual(result, expected)

    def test_get_max_salary_per_razdel(self):
        result = self.manager.get_max_salary_per_razdel()
        expected = [
            ("Анализ", 70000),
            ("Бухгалтерия", 60000),
            ("Маркетинг", 55000),
        ]
        self.assertEqual(result, expected)

    def test_get_all_linked_data(self):
        result = self.manager.get_all_linked_data()
        expected = [
            ("Анализ", "Анализ рынка"),
            ("Анализ", "Отчет по продажам"),
            ("Бухгалтерия", "Финансовый отчет"),
            ("Маркетинг", "План продаж"),
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
        unittest.main()


# Пример использования

