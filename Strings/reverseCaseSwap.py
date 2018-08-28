def caseSwapAndReverse(inp):
    revstr=""
    for x in inp:
        revstr = x+revstr
    revstr = revstr.swapcase()
    return revstr

print(caseSwapAndReverse("Hello Python World"))