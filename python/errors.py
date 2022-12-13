''' errors are of many types 
        syntax error: the one which does not display the output and also gives
        some line number for reference.
        
        runtime error: is when you get some result like 10/0

        logical error: is the error from the user side and is not easy to find 
        and fix. The best method to solve the error is using print and dry 
        running the code.  '''

''' exception handeling: is used to test the code which is under suspicion and 
    if the error that you mentioned occurs then the code will not be executed
    and instead the alternate code in the except block will run.
'''
try:
    # the code under suspicion
except:
    # the alternate code 

''' also you can have multiple except blocks 
    but you have to be more specific about the exception
    and an else at the end for the case where all the specified possibilities
    fail and there is another block called finally and it will definitely 
    execue
'''
''' 
try:
    age = int(input("enter the age: "))

'''


