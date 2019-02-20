#inheritance
class Animal():

    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

'''
mya = Animal()
mya.whoAmI()
mya.eat()
'''

'''
class Dog(Animal):

    def __init__(self):
        #Animal.__init__(self)
        print("Dog created")

mydog = Dog()
mydog.whoAmI()
mydog.eat()
'''

class Dog(Animal):

    def __init__(self):
        #Animal.__init__(self)
        print("Dog created")

    def bark(self):
        print("woof")

    #override : vai entrar no lugar do de cima pq tem o mesmo nome
    def eat(self):
        print("dog eating")

mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()
mydog.eat()

#special methods
'''
mylist = [1,2,3]
print(mylist)

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

b = Book("Python", "Jose", 200)
print(b)
'''

'''
mylist = [1,2,3]
print(mylist)

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    #representacao da string (ex:print)
    def __str__(self):
        return "hello"

b = Book("Python", "Jose", 200)
print(b)
'''

'''
mylist = [1,2,3]
print(mylist)

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    #representacao da string (ex:print)
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

b = Book("Python", "Jose", 200)
print(b)

print(len([1,2,3]))
#print(len(b))
'''

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    #representacao da string (ex:print)
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is destroyed!")

b = Book("Python", "Jose", 200)
print(b)
print(len(b))
del b

mylist = [1,2,3]
print(mylist)
print(len(mylist))
