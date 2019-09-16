#Write a function that takes a string as input argument and returns a dictionary of letter counts 
# i.e. the keys of this dictionary should be individual letters and the values should be the total count 
# of those letters. You should ignore white spaces and they should not be counted as a character. 
# Also note that a small letter character is equal to a capital letter character.

def letterCount(inp):
    dicti = {}
    #inp = ""
    inp = inp.lower()
    inp = inp.replace(' ','')
    for i in range(len(inp)):
        print(inp)
        c = inp[i]
        dicti.setdefault(c,inp.count(c))
        inp.replace(c,'')
        print(dicti)
    return dicti

print(letterCount("asvbsdsdb sdksljdsa"))