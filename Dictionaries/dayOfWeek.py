from math import *

def dayOfWeek(inpstr):
    daysDict = {0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}
    monDict = {"January":11,"February":12,"March":1,"April":2,"May":3,"June":4,"July":5,"August":6,"September":7,"October":8,"November":9,"December":10}
    w=0
    slist = inpstr.split()
    d = int(slist[1])
    m = int(monDict.get(slist[0]))
    
    c = int(slist[2][:2])
    y = int(slist[2][2:])
    if m > 10:
        y = y - 1
    w = (d + floor(2.6*m - 0.2) -2*c + y + floor(y/4) + floor(c/4)) % 7
    return daysDict.get(w)

print(dayOfWeek("January 1 1678"))