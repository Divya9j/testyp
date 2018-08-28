def sumASCII(inp):
    sum=0
    for a in inp:
        sum = sum + ord(a)
    return sum

print(sumASCII("hello"))