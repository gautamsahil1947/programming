''' this is the master file of the calculator and the functions are defined in the other file called function and this file deals with
    the user interface more that is what to prompt and what to take input. 
    the capabilities of this calculator are
        sum
        product
        difference
        remainder
        factorial
        determinant 2x2 3x3
        and trigonometric calculations like sin cos and also the inverses
        '''
# this is the prompt for the user to choose the operation 
a = '''choose the operation.
        1. sum
        2. product
        3. exponent
        4. remainder
        5. factorial
        6. 2 x 2 determinant
        7. 3 x 3 determinant
        8. sine  
        9. cosine 
        10. tangent  
        11. degree to radian
        12. radian to degree

        '''
import function
# the line above imports the function file where all the functions are defined.
print(a)
i = int(input("Enter the option: "))

''' so all the function related stuff including the prompt for input for the values are defined in the other file called function.py, and so here we just check for the
    choice and redirect the user to that specific funcion.'''
if ( i == 1):
    function.sumation()
elif ( i == 2):
    function.product()
elif ( i == 3):
    function.exponent()
elif ( i == 4):
    function.remainder()
elif ( i == 5):
    function.factorial()
elif ( i == 6):
    function.determinant_2x2()
elif ( i == 7):
    function.determinant_3x3()
elif ( i == 8):
    function.sine()
elif ( i == 9):
    function.cosine()
elif ( i == 10):
    function.tangent()
elif ( i == 11):
    function.detorad()
elif (i == 12):
    function.radtode()
''' so this is a note for future reference that only the if and the elif conditionals take the conditions and the else block doesn't 
    take care of this in future.'''
    # so do not enter any condition in the else.
