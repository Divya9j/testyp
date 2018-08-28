
def multi2DList(X,Y):
    acol = len(X[0])
    brows = len(Y)
    result=[]
    temp_row=len(Y[0])*[0]
    for r in range(len(a)):
        result.append(temp_row[:])
    if acol == brows:
        for i in range(len(X)):
       # iterate through columns of Y
            for j in range(len(Y[0])):
                # iterate through rows of Y
                for k in range(len(Y)):
                    result[i][j] += X[i][k] * Y[k][j]
    return result


a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

print(multi2DList(a,b))