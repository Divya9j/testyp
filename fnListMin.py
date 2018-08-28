def test(x):
    lesser=x[0]
    for begin_num in x :        
        if(lesser > begin_num):
            lesser = begin_num
    return lesser

# Main Program
my_list=[6,2,3,4,5]
print(test(my_list))