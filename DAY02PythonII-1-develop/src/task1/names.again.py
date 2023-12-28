# Допиши класс Student
# В классе два поля: name, surname
# И два метода: __init__, get_full_name
class Student:
    
    # Инициализируй поля name и surname (НО сначала опиши их в классе)
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    # Метод должен возвращать строку следующего вида
    # "name surname"
    # пробел обязателен!
    def get_full_name(self):
        get_full_name = self.name + ' ' + self.surname
        return get_full_name

# Считай имена из файла names.txt
# И создай на каждую строку по объекту класса Student
lst = []
with open('materials/task1/names.txt', 'r') as file:
    for line in file.readlines():
        lst_full_name = line.strip().split()
        lst.append(Student(lst_full_name[0], lst_full_name[1]))

# print(lst)    
lst.sort(key=lambda x: x.name)

# Отсортируй студентов в алфавитном порядке
# Запиши в файл sorted_names.txt
with open('src/task1/sorted_names.txt', 'w') as file:
    for student in lst:
        print(f"{student.get_full_name()}", end='\n', file=file)

# Создай словарь: ключ - Имя, значение - сколько раз встречается в файле names.txt ЧТО ЗА БРЕД? НУ ОК
dict_students = {}
for student in lst:
    dict_students[student.name] = dict_students.setdefault(student.name, 0) + 1

# for name, count in dict_students.items():
#     print(f"{name}-{count}")