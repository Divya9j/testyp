def unique_common(a, b):
    cList=[]
    for i in a:
        for j in b:
            if j == i:
                if cList.count(j) == 0:
                    cList.append(j)
    cList.sort()
    return cList

print(unique_common([5, 6, -7, 8, 8, 9, 9, 10], [2, 4, 8, 8, 5, -7]))