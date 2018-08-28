def trimspace(inp):
    idx=0  
    x= len(inp)  
    while x >0:
        #print(ord(x))
        if (ord(inp[x-1]) != 32):
            idx = x
            break
        x=x-1
    #print(count)
    return inp[:idx]

print(trimspace('    abc  '))