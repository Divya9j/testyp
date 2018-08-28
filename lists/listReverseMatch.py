def crazy_list(some_list):
    l = len(some_list)
    crazy=False
    count=0
    for i in range(0,l):
        #print(some_list[i])
        #print(some_list[l-(i+1)])
        if(some_list[i] == some_list[l-(i+1)]):
            count = count+1
    if count == l :
        return True
    else:
        return False

crazy_list([4, 5, 6, 7, 8, 4, 5, 2])