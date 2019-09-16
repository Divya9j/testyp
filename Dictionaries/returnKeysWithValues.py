#Write a function named return_keys which accepts a dictionary and an integer as input and returns
#  an ascending sorted list of all the keys whose values contain the input integer. Note that the keys of 
# this dictionary are strings while the values of this dictionary are 1 Dimensional lists of integers

def return_keys(sample_dictionary, sample_value):
    rl = []
    #vals = list(sample_dictionary.values())
    vals = sample_dictionary.keys()
    for val in vals:
        lst = list(sample_dictionary.get(val))
        if lst.count(sample_value) != 0:
            rl.append(val)
    rl.sort()
    return rl

sample_dictionary = {"rabbit" : [1, 2, 3],
          "kitten" : [2, 2, 6],
          "lioness": [6, 8, 9]}

print(return_keys(sample_dictionary,2))