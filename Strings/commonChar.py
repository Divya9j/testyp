def commonChar(inp):
    inp = inp.lower()
    cchar=""
    cnt = 0
    prevcnt = 0
    for x in inp:
        if x != " ":
            cnt = inp.count(x)
            print(x,cnt)
            if cnt >= prevcnt:
                cchar = x
                prevcnt = cnt
    return cchar
        

print(commonChar("ya gotta make do with what ya got"))