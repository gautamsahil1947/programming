''' this is tuples '''
# tuple is represented as a = (some data and comma)
'''
tuple is like a list but it is a read only list.
and it is immutable and one can only read data 
and also the tuples are faster than list as the computer only reads them

you can use the fn type(data) to find the data type of the data.

and a = (1) is a special case which is when you are working with one elemented tuple, you have to end the element with comma instead of nothing.
    a = (1,) this is a tuple
    a = (1) is an integer

hi sahil go to geeks for geeks to understand in depth the things like fns and the other stuff

'''


''' 
    Question : you are given a tuple and your task is to update the first element of the tuple, how would you do it.
'''
# this is the given tuple
a = (1, 2, 3, 4, 5)
# we converted the tuple to a list
j = list(a)
# changed the element that you want to change
j[0] = 6
# print the new list as a tuple
print(tuple(j))
# (6, 2, 3, 4, 5) this is the output.

'''
Question : what if the element inside the tuple is a list and you try to change the element in that list
'''
# it works
'''
Question : take user input --- convert it to tuple --- ask for the index from the user --- print the value at that index ---- else if the index is out of tuple print invalid index
'''
# the first line is taking input as a string,
# and splits it into a list of integers
# and then converts the list of strings to a list of integers
# and then converts the list to a tuple
i = tuple(int(j) for j in input("enter the data: ").split(","))
# this line takes the input for the index value from the user which we are supposed to fetch
k = int(input("enter the index: "))
# this condition checks whether the index is in range or not
if (-len(i) <= k <len(i)):
    # if the index is in the range then it prints the value at that index
    print(i[k])
else:
    # if not then this line prints "Index out of range" 
    print("Index out of range.")

# and this works for the integer inputs and also the input should not have a comma or a space at the end. 

# dictionaries are unodered and work on the basis of the key value basis.
# so the indexing will not work here
'''
    and the key should be unique in nature and the value can repeate
    inside a dictionary there can be another dictionary but the thing is that the nested dictionary should be the value and not the key 
    dictionary is mutable data type . 
    
    also note that in order to fetch the values in the dictionary you have to use the key as the index and 
        nameofthedictionary[key of the value as it is.]
    
    '''
    