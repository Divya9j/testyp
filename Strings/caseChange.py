def caseChange(inp):
    newstr=""
    for x in inp:        
        if ((ord(x) >= 97 and ord(x) <= 122)):
            newstr = newstr + chr(ord(x)-32)
        elif ((ord(x) >= 65 and ord(x) <= 90)):
            newstr = newstr + chr(ord(x)+32)
        else:
            newstr=newstr+x
    return newstr

print(caseChange("HeLlo 4 efdfv"))