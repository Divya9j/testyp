def items_price(a, b):
    sum = 0
    for i in range(0,len(a)):
        sum = sum + (a[i]*b[i])
    return sum

a = [2, 3, 5, 7, 9]
b = [5, 8, 4, 1, 11]

print(items_price(a,b))