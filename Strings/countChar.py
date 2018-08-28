def countChar(inp,c):
    inp = inp.lower()
    c = c.lower()
    cnt = 0
    for i in inp:
        if i == c:
            cnt = cnt+1
    return cnt

print(countChar("abdcsas","A"))