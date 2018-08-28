def test(x):
    sum=0
    for begin_num in x :
        sum = sum+begin_num
    return sum

# Main Program
my_list=[1,2,3,4,5]
print(test(my_list))