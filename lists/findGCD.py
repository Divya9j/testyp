def find_gcd(some_list):
    gcd=1
    for cnt in range(2,max(some_list)):
        gcdCnt=0
        for num in some_list:
            #print(num, cnt, num%cnt)
            if num%cnt == 0:
                gcdCnt = gcdCnt +1
        #print("gcdcnt ",gcdCnt)
        if gcdCnt == len(some_list):
                gcd = cnt
    return gcd

find_gcd([3, 5, 9, 11, 13])