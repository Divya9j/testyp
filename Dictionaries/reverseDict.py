#Write a function named "reverse_dictionary" that receives a dictionary as input argument and returns a reverse
#  of the input dictionary where the values of the original dictionary are used as keys for the returned dictionary 
# and the keys of the original dictionary are used as value for the returned dictionary 

def reverse_dictionary(input_dict):
    rd = {}
    klist = input_dict.keys()
    for k in klist:
        lst = list(input_dict.get(k))
        
        for l in lst:  
            vlist = []
            l = l.lower()                   
            if rd.get(l,"None") == "None":
                vlist.append(k.lower())
                rd.setdefault(l,vlist)
            else:
                vlist = list(rd.get(l))
                print(l, k, vlist, vlist.count(k))
                if vlist.count(k) == 0:
                    vlist.append(k)
                    vlist.sort()
                upddict = {l: vlist}
                rd.update(upddict)
            print(rd)
    return rd

print(reverse_dictionary({'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}))