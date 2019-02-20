'''
class Grain():
    
    def __init__(self):
        pass

mygrain = Grain()
print(type(mygrain))
'''

'''
class Grain():
    
    def __init__(self, specie):
        self.specie = specie

mygrain = Grain(specie = "Serjania")
print(type(mygrain))
print(mygrain.specie)

otherGrain = Grain(specie = "Bauhinia")
print(otherGrain.specie)
'''

'''
class Grain():
    
    def __init__(self, family, specie):
        self.family = family
        self.specie = specie

#mygrain = Grain(family='X', specie='Bauhinia')
mygrain = Grain('X', 'Bauhinia')
print(mygrain.family)
print(mygrain.specie)
'''

'''
class Grain():
    
    #class object attribute
    ordem = "pollen"

    def __init__(self, family, specie):
        self.family = family
        self.specie = specie

#mygrain = Grain(family='X', specie='Bauhinia')
mygrain = Grain('X', 'Bauhinia')
print(mygrain.ordem)
print(mygrain.family)
print(mygrain.specie)
'''

'''
class Circle():
    
    pi = 3.14

    #default value = não precisa declarar na hora de chamar se já tem
    def __init__(self, radius=1):
        self.radius = radius

myc = Circle()
print(myc.radius)
'''

'''
class Circle():
    
    pi = 3.14

    #default value = não precisa declarar na hora de chamar se já tem
    def __init__(self, radius=1):
        self.radius = radius

    #self aqui significa que é um método dessa classe
    def area(self):
        #return radius*radius*pi
        return self.radius*self.radius*Circle.pi

myc = Circle()
print(myc.radius)

myc = Circle(3)
print(myc.radius)
print(myc.area)
print(myc.area())
'''

class Circle():
    
    pi = 3.14

    #default value = não precisa declarar na hora de chamar se já tem
    def __init__(self, radius=1):
        self.radius = radius

    #self aqui significa que é um método dessa classe
    def area(self):
        #return radius*radius*pi
        return self.radius*self.radius*Circle.pi

    def set_radius(self, new_radius):
        self.radius = new_radius

myc = Circle()
print(myc.radius)

# programming style choice
myc = Circle(3)
#myc.radius = 100
myc.set_radius(100)
print(myc.radius)
print(myc.area())