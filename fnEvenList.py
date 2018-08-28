def test(x):
    even_list=[]    
    for begin_num in x :        
        if(begin_num%2 == 0):
            even_list.append(begin_num)
    return even_list

# Main Program
my_list=[1,2,3,4,5]
print(test(my_list))