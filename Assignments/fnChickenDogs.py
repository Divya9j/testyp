def countChickenDogs(heads,legs):
    chickens=0
    dogs=0
    while(True):
        #print(chickens,dogs,heads,legs)
        chickens = chickens+1
        heads = heads -1
        legs = legs - 2
        #print(chickens,dogs,heads,legs)
        if(legs >= 4 and heads >= 1 and legs != heads*2):
            dogs = dogs +1
            heads = heads -1
            legs = legs - 4
            #print(chickens,dogs,heads,legs)
        if(heads == 0 or legs == 0):
            break
    if(heads == 0  and legs == 0):
        return([chickens,dogs])

print(countChickenDogs(6,18))

