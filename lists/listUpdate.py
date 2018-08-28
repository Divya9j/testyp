def updateList(inpList, inpStr):
    beginNum=1
    endNum=len(inpList)-1
    while(beginNum != endNum):
        inpList[beginNum]=inpStr
        beginNum = beginNum+1
    return inpList

print(updateList(["Isha", "Chandoygya", "Sri Vasya", "Mandukya", "Sri"],"Brahman"))