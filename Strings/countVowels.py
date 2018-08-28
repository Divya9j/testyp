def countVowels(inp):
    inp = inp.lower()
    cnt = 0
    for i in inp:
        #print(i)
        if i == "a" or i == "e" or i == "i" or i=="o" or i == "u":
            cnt = cnt +1
    return cnt

print(countVowels("asnbdnsdE"))