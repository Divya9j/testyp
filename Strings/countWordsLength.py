def countWordsLen(inp):
    slist = inp.split()
    cnt=0
    #print(slist)
    for wrd in slist:
        if len(wrd)>4:
            cnt = cnt +1
    return cnt

print(countWordsLen("Thise"))