def test(veclist):
    exprval = pow(veclist[0],2) + pow(veclist[1],2) + pow(veclist[2],2)
    return sqrt(exprval)

def sqrt(inp):
    guess = inp/2;
    accuracy = 0.01;
    iteration=0;
    while abs(inp-(guess**2)) > accuracy :
        guess = (guess+(inp/guess))/2;        
        iteration=iteration+1;
    return guess

# Main Program
veclist = [2,3,-4]
print(test(veclist))

