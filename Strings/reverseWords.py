def reverseWords(inp):    
    inpList = inp.split()
    revList=[]
    retstr=""
    for wrd in inpList:   
        revstr=""
        print(wrd)     
        for x in wrd:
            revstr = x+revstr
        revList.append(revstr)
    for w in revList:
        retstr = retstr + w +" "
    retstr = retstr.rstrip()
    return retstr


print(reverseWords("this is a sample test"))