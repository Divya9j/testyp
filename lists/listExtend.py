def listExtend(list1, list2):
    newList=[]
    for x in list1:
        newList.append(x)
    for x in list2:
        newList.append(x)
    return newList

A = ['p', 'q', 6, 'k']
B = [8, 10]
print(listExtend(A,B))