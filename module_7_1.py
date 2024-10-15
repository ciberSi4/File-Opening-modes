# Домашнее задание по теме "Режимы открытия файлов"
class Product:
    def __init__(self, name, weight, category):
        self.name : str = name
        self.weight : float = weight
        self.category : str = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = "products.txt"
        f = open(self.__file_name, "a")
        f.close()

    def get_products(self):
        file = open(self.__file_name, "r")
        product_line = file.read()
        file.close()
        return product_line

    def add(self, *products : Product):
        for product in products:
            if f"{product}" in self.get_products():
                print(f"Продукт {product} уже есть в магазине")
            else:
                file = open(self.__file_name, "a")
                file.write(f"{product}\n")
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())