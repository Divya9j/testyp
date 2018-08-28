def remList(inpList) :
    retList=[]
    beginNum=0
    for x in inpList:
        if(beginNum == 0 or beginNum%2==0):
            retList.append(x)
        beginNum = beginNum + 1

    return retList

input_list = ["we", "love", "python", "so","much"]
print(remList(input_list))