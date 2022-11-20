''' Question 
    make a function which takes inputs from the user one after the other.
    if the input is 'result' then print the sum of the values entered before
    if the input is a number then add it to the other input numbers
    if the input is a string other than result then print invalid input. 
    
    sample inputs and outputs:
    you run the code
    choose the option: 1
    input: 1
    input: 2
    input: 3
    input: 55.5
    input: result
    sum : 61.5

    you run the code
    choose the option: 1
    input: 2
    input: 2
    input: 3
    input: 55
    input: sahil
    invalid input.

    '''
def sumation():
    b = '''initially sum = 0
           at the prompt input: , enter the value and that value will be added to sum
           to print the sum the input should be result.'''
    def valid(k):
        count = 0
        for m in k:
            if (m == "."):
                count += 1
        for m in k:
            if (not('0' <= m <= '9') or count not in (0, 1)):
                return "String"
        return "Number"

    print(b)
    sum = 0
    while (True):
        i = (input("input: "))
        if (i == "result"):
            print("sum:",sum)
            break
        elif (i != "result" and valid(i) == "String"):
            print("invalid input.")
            break
        else:
            sum = sum +  float(i)

# so the above code had a bug where it is not able to take float inputs

''' Thought Process/ pseudocode
    forever
        take input from the user
        if input == number
            add to sum variable
        elif input == result
            print the sum
        else input is a string other than result
            print invalid input
'''

def product():
    b = ''' enter the inputs to multiply
            enter 0 to print result.'''
    print(b)
    pro = 1
    while (True):
        i = float(input("input: "))
        if (i != 0):
            pro *= i 
        else:
            print(pro)
            break 

def exponent():
    b = ''' the first number entered will be base and the next inputs will be the exponents.'''
    print(b)

    def valid(k):
        count = 0
        for m in k:
            if (m == "."):
                count += 1
        for m in k:
            if (not('0' <= m <= '9') or count not in (0, 1)):
                return "String"
        return "Number"

    exp = "no value entered."
    j = input("enter the first base: ")
    m = 0
    while (m < 1):
        
        if (j == "result"):
            print("answer: ",exp)
            break
        elif (j != "result" and valid(j) == "String"):
            print("invalid input.")
            break
        else:
            exp = float(j)
        m += 1


    while (True):
        i = (input("input: "))
        if (i == "result"):
            print("answer: ",exp)
            break
        elif (i != "result" and valid(i) == "String"):
            print("invalid input.")
            break
        else:
            exp = exp ** float(i)


