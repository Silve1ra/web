#LEGB Rule
#local
#enclosing function locals
#global
#built-in

x = 25

def my_func():
    x = 50
    return x

print(x)
print(my_func())
print(x)
my_func()
print(x)

# LOCAL
lambda x: x**2

# Enclosing function locals
name = 'this is a global name'

def greet():
    name = 'sammy'

    def hello():
        print("hello " + name)

    hello()

greet()
print(name)

#built-in
#len = 23

# local variables
x = 50

def func(x):
    print('x is: ', x)
    x = 1000
    print('local x is: ', x)

func(x)
print(x)

def func2():
    global x
    x = 1000

print('before: ', x)
func2()
print(x)

def func3():
    x = 1000
    return x

x = func3()
print(x)