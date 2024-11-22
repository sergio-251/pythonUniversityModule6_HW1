# Зачем нужно наследование

class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        s = 'съел' if food.edible else 'не стал есть'
        self.fed = True if food.edible else False
        self.alive = True if food.edible else False
        print(self.name, s, food.name)


class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        self.edible = True
        self.name = name

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)