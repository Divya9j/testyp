def pattern_sum(a, b):
    sum=0
    pattern=[1,11,111,1111,11111,111111,1111111,11111111,111111111]
    for i in range(1,b+1) :
        #print(pattern[i-1])
        sum = sum + (a * pattern[i-1])
        #print(sum)
    return sum

print(pattern_sum(3,4))