class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        
    
    def go_to(self, new_floor) -> int:
        self.new_floor = new_floor
        if self.new_floor <= self.number_of_floors: 
            for i in range(new_floor):
                print(i + 1)
        else:
            print('Нет такого этажа')
            
    def __len__(self):
        return self.number_of_floors
        
    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
