#numbers, strings, lists, dictionaries
#tuples, sets, booleans
#control flow
#functions

#scope
#POO
#errors and exceptions
#decorators
#regular expressions

#strings
#basics
'hello'
"hello"

#indexing
mystring='abcdefg'
print(mystring[-1])
print(mystring[-2])
print(mystring[0])

#slicing
print(mystring[2:])
print(mystring[:3])
print(mystring[2:5])
print(mystring[:])
print(mystring[::])
print(mystring[::1])
print(mystring[::2])

#
#mystring[0] = 'X'
mystring='abcdefg'
#mystring='X'

x = mystring.upper()
print(x)

x = mystring.lower()
print(x)

x = mystring.capitalize()
print(x)

x = mystring.upper()
print(x)

mystring='Hello World'
x = mystring.split()
print(x)

mystring='Hello World'
x = mystring.split('e')
print(x)

x = "Insert another string here: {}".format("INSERT ME!")
print(x)

x = "Item one: {} Item two: {}".format("dog", "cat")
print(x)

x = "Item one: {x} Item two: {y}".format(x="dog", y="cat")
print(x)

x = "Item one: {y} Item two: {x}".format(x="dog", y="cat")
print(x)