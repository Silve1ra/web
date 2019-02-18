#greater than
1>2

#less than
1<2

1>=1

1<=4

#equality
1==1
1 == '1'

'hi' == 'bye'

#inequality
1 != 2

#logical operators
#and
(1>2) and (2<3)

#or
(1>2) or (2<3)

#multiple logical operators
(1==2) or (2==3) or (4==4)

#identation
if 1<2 :
    print('yes')

if 1<2:
    print('first block')
    if 4<3:
        print('second block')


if 1<2:
    print('hello')
else:
    print('last')

if 1>2:
    print('hello')
elif 3 ==3  :
    print('elif ran')
else:
    print('last')



# for loops
seq = [1,2,3,4,5,6]

for item in seq:
    print(item)

#sem ordem (dicts)
d = {'Sam':1, 'Frank':2, 'Dan':3}

for item in d:
    print(item)


for k in d:
    print(k)
    print(d[k])

for k in d.keys():
    print(k)

for k in d.values():
    print(k)


mypairs = [(1,2),(3,4),(5,6)]

for item in mypairs:
    print(item)

for (tup1, tup2) in mypairs:
    print(tup2)
    print(tup1)
    

#while
i = 1

while i<5:
    print('i is: {}'.format(i))
    i = i+1


#range
x = list(range(0,5))
print(x)

x = list(range(0,20,2))
print(x)

for item in range(10):
    print(item)


#list comprehension
x = [1,2,3,4]
out = []

for num in x:
    out.append(num**2)

print(out)

print([num**2 for num in x])