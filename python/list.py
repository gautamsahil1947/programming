# this file is about list comprehension.
# this list will take a single universal input and demonstrate all the list comprehensions on it.




print(list(int(i) for i in input("enter the space seperated list: ").split(" ")))
    # so as expected this prints the list of the input entered by the user.


# print(list(int(i) for i in input("enter the space seperated list: ") if (int(i) % 2 == 0)))
    # so this should print the list of even inputs in the input.
    ''' the line above has an error  which is taht i didn't break the input into the list and this made the interpretor 
        show error'''


