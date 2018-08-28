def cntWords(inp,c):
    inpl = inp.lower().split()
    c=c.lower()
    cnt=0
    #print(inpl)
    for wrd in inpl:
        if wrd[0] == c:
            cnt = cnt +1
    return cnt

print(cntWords("Ths Sis a String","s"))