class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        temp = [line.replace('\n', ' ') for line in file]
        file.close()
        return '\n'.join(temp)

    def add(self, *products):
        file = open(self.__file_name, 'a+')
        for c in products:
            file.seek(0)
            if c.name not in file.read():
                file.write(str(c))
                file.write('\n')
            else:
                print(f'Продукт {c.name} уже есть в магазине')

        file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Popcorn', 5.5, 'Vegetables')
p5 = Product('Sandaly', 5.5, '1111')

print(p2) # __str__

s1.add(p1, p2, p3, p4, p5)

print(s1.get_products())
