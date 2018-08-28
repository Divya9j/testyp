def removeSpaces(inp):
    newstr=""
    for x in inp:
        if(ord(x) != 32):
            newstr = newstr+x
    return newstr