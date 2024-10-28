# Домашнее задание по теме "Режимы открытия файлов"
# Если вы решали старую версию задачи, проверка будет производиться по ней.
# Ссылка на старую версию тут.
#
# Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.
#
# Задача "Учёт товаров":
# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и обладать следующими свойствами:
# Атрибут name - название продукта (строка).
# Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
# Атрибут category - категория товара (строка).
# Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены запятой с пробелами.
#
# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
# Инкапсулированный атрибут __file_name = 'products.txt'.
# Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
# Метод add(self, *products), который принимает неограниченное количество объектов класса Product. Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию). Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
#
# Пример результата выполнения программы:
# Пример работы программы:
# s1 = Shop()
# p1 = Product('Potato', 50.5, 'Vegetables')
# p2 = Product('Spaghetti', 3.4, 'Groceries')
# p3 = Product('Potato', 5.5, 'Vegetables')
#
# print(p2) # __str__
#
# s1.add(p1, p2, p3)
#
# print(s1.get_products())
#
# Вывод на консоль:
# Первый запуск:
# Spaghetti, 3.4, Groceries
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
# Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato, 50.5, Vegetables уже есть в магазине
# Продукт Spaghetti, 3.4, Groceries уже есть в магазине
# Продукт Potato, 5.5, Vegetables уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
# Как выглядит файл после запусков:
#
#
#
# Примечания:
# Не забывайте при записи в файл добавлять спец. символ перехода на следующую строку в конце - '\n'.
# При проверке на существование товара в методе add можно вызывать метод get_products для получения текущих продуктов.
# Не забывайте закрывать файл вызывая метод close() у объектов файла.
#
# Файл module_7_1.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
# Успехов!


# module_7_1.py

# Домашнее задание по теме "Режимы открытия файлов"

# Задача "Учёт товаров"

# Класс Product
class Product:
    def __init__(self, name, weight, category):
        # Атрибут name - название продукта (строка).
        self.name = name
        # Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
        self.weight = weight
        # Атрибут category - категория товара (строка).
        self.category = category

    def __str__(self):
        # Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
        # Все данные в строке разделены запятой с пробелами.
        return f'{self.name}, {self.weight}, {self.category}'


# Класс Shop
class Shop:
    # Инкапсулированный атрибут __file_name = 'products.txt'.
    __file_name = 'products.txt'

    def get_products(self):
        # Метод get_products(self), который считывает всю информацию из файла __file_name,
        # закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return 'Ошибка «Файл не найден».'

    def add(self, *products):
        # Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
        existing_products = self.get_products().split('\n')
        # Имена продуктов записываются в existing_product_names. Так как строки в файле имеют формат
        # '<название>, <вес>, <категория>', то берется первая часть [0]. В качестве разделителя используется ', '.
        # Для добавления, если строка line не пустая, цикл for перебирает все строки из списка existing_products.
        existing_product_names = {line.split(', ')[0] for line in existing_products if line}

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name in existing_product_names:
                    # Если такой продукт уже есть, то не добавляет и выводит строку
                    # 'Продукт <название> уже есть в магазине'.
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    # Добавляет в файл __file_name каждый продукт из products,
                    # если его ещё нет в файле (по названию).
                    file.write(str(product) + '\n')
                    existing_product_names.add(product.name)


# Пример работы программы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
