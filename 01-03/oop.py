class hero:

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = hero("sniper",100, 10, 4)
hero2 = hero("nana", 85, 50, 0)
hero3 = hero("budi", 150, 8, 10)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)