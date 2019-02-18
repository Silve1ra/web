#functions (def)
def my_func(param1='default'):
    """
    THIS IS DOCSTRING
    """

    print('function {}'.format(param1))


def hello():
    print('hello')

def hello2():
    return 'hello'

my_func()
hello()

hello2()
result = hello2()
print(result)


def addNum(num1, num2):
    return num1+num2

result = addNum(2,3)
print(result)

result = addNum("2","3")
print(result)
print(type(result))


def addNum2(num1, num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry"

result = addNum2("2","3")
print(result)

#lambda expression

#filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, mylist)
print(list(evens))
print(evens)


evens = filter(lambda num:num%2 == 0, mylist)
print(list(evens))

st = 'hello'
st.lower()
st.upper()
st.split()

tweet = "Go sports! #Sports"
result = tweet.split('#')
print(result)

result = tweet.split('#')[1]
print(result)

print('x' in [1,2,3])