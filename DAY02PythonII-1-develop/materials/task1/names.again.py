# Допиши класс Student
# В классе два поля: name, surname
# И два метода: __init__, get_full_name
class Student:
    
    # Инициализируй поля name и surname (НО сначала опиши их в классе)
    def __init__(self, name, surname):
        pass

    # Метод должен возвращать строку следующего вида
    # "name surname"
    # пробел обязателен!
    def get_full_name(self):
        pass

# Считай имена из файла names.txt
# И создай на каждую строку по объекту класса Student
with open('materials/task1/names.txt', 'r') as file:
    pass

# Отсортируй студентов в алфавитном порядке
# Запиши в файл sorted_names.txt
with open('src/task1/sorted_names.txt', 'w') as file:
    pass

# Создай словарь: ключ - Имя, значение - сколько раз встречается в файле names.txt
