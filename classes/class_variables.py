class Student:
    school = "ABC School"

s1 = Student()
s2 = Student()
print(s1.school, s2.school)


class Item:
    count = 0
    
    def __init__(self):
        Item.count += 1

Item()
Item()
print(Item.count)


class Config:
    debug = True

print(Config.debug)
Config.debug = False
print(Config.debug)


class Player:
    total = 0
    
    def __init__(self, name):
        self.name = name
        Player.total += 1

Player("Tom")
Player("Ann")
print(Player.total)
