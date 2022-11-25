# a = {6: 'six', 7: 'seven', 1: 'one'}
# print(all(a))
# ''' this checks whether any of the keys is zero or not and if it finds a key zero and if it findes a zero, then it returns
#     '''
# print(any(a))
# len(a)
# sorted(a)







# ''' take an integer seq from the user and write a programm to print a dictionary from the entered sequence.
#     which has tuples and the key value paris are the number by the user and the count of the number in the'''
# k = list(int(i) for i in input("Enter the values: ").split(","))
# def count(n):
#     c = 0
#     for j in k:
#         if j == n:
#             c += 1
#     return c

# l = {}
# for o in k:
#     l[o] = count(o)
# print(l.items())

# Enter the values: 1,2,3,4
# dict_items([(1, 1), (2, 1), (3, 1), (4, 1)])

# # and this is the output of the code




''' these are the dictionary inbuilt functions.
    a.len()
    a.clear()
    dict.fromkeys(c, 10)
    a.get(key)
    a.setdefault(k, four)
    a.update(b) where a and b are two seperate dictionaries.
    a.keys() this will return all the keys in terms of values
    a.values() will return a list of all the values
    a.items() will return a list of tuples of all the key value pairs.
    
    dictionary comprehension this is to do on your  '''




