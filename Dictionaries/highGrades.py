def highGrades(dicti):
    klist = dicti.keys()
    nlist=[]
    for k in klist:
        lst = dicti.get(k)
        if lst[0] >= 78 and lst[1] >= 78 and lst[2] >= 78:
            nlist.append(k)
    return nlist

d={'a':[10,20,50]}
print(highGrades(d))