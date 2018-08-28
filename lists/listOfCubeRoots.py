def cubeRootsList(x):
    myList=[]    
    for beginNum in range(1,x) :
        myList.append(beginNum**(1./3.))
    return myList

print(cubeRootsList(4))