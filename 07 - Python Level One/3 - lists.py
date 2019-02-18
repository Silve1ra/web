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

#remove thin
mylist = ['a', 'b', 'c', 'd', 'e']
item = mylist.pop()
print(mylist)
print(item)

mylist = ['a', 'b', 'c', 'd', 'e']
item = mylist.pop(0)
print(mylist)
print(item)

mylist.reverse()
print(mylist)

mylist = [4,1,8,4,0,45]
mylist.sort()
print(mylist)

#lista aninhada
mylist = [1, 2, ['x', 'y', 'z']]
print(mylist[2])
print(mylist[2][1])

#lista de compressao
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[0][0])

first_col = [row[0] for row in matrix]
print(first_col)