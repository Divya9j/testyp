def sortedList(inpList):
    srtList=[]
    for wrd in inpList:
        srtList.append(wrd)    
    srtList.sort()
    print(inpList)
    if srtList == inpList:
        return True
    else:
        return False

print(sortedList(["aa","be","cr"]))