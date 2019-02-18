mylist = [1,2,3]
mylist = ['ola', 123, True, 23.3, [1,2,3]]
print(mylist)
print(len(mylist))

mylist = ['a', 'b', 'c']
print(mylist[0])
print(mylist[-1])

mylist = ['a', 'b', 'c', 'd', 'e']
print(mylist[1:])
print(mylist[:3])

mylist[0] = 'NEW ITEM'
print(mylist)

mylist.append("New item 2")
print(mylist)

mylist.append(['x', 'y', 'z'])
print(mylist)

listone = ['a', 'b', 'c']
listtwo = ['x', 'y', 'z']
listone.extend(listtwo)
print(listone)