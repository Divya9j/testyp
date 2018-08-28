def multiChk(a,b):
    acol = len(a[0])
    brows = len(b)
    if acol == brows:
        return True
    else:
        return False


a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

print(multiChk(a,b))