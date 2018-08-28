def triangle(height):
    
    i = height
    while i >=1 :
        astr="*"
        if i == height or i == 2 or i==1:
            print(astr*i)
        else:         
            print(astr+" "*((i-2))+astr)
        i=i-1

triangle(1)