def palindrome(inp):
    inpc = inp.lower()
    i = len(inp)
    cnt = 0
    for j in range(0,len(inp)):
        if inpc[i-1] == inpc[j] :
            cnt = cnt + 1 
        i= i -1
    if cnt == len(inp):
        return True
    else:
        return False
print(palindrome("adcdA"))