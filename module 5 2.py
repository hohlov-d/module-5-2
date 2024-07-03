class House:
    def __init__(self, name, number_of_flours):
        self.name = name
        self.number_of_floors = number_of_flours
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название {self.name}, кол-во этажей {self.number_of_floors}'


h1 = House('ЖК Ботаника', 20)
h2 = House('Бирюзовая', 5)
#_str_
print(h1)
print(h2)
#_len_
print(len(h1))
print(len(h2))