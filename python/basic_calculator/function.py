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


def remainder():
    b = ''' a = first input
            b = second input
            result = a % b'''
    c = float(input("a: "))
    d = float(input("b: "))
    print("result :" , c % d)





def factorial():
    def fac(n):
        if (n == 1):
            return 1
        else:
            return n * fac(n - 1)
    
    while (True):
        k = int(input("enter the natural number: "))
        if (k > 0 and k % 1 == 0):
            break
        else:
            continue
    print(fac(k))




def determinant_2x2():
    b = '''    a11   a12 
    a21   a22 '''
    print(b)
    a11 = float(input("a11: "))
    a12 = float(input("a12: "))
    a21 = float(input("a21: "))
    a22 = float(input("a22: "))

    g = (a11 * a22) - (a21 * a12)
    print("vlaue of determinant is:" , g)


def determinant_3x3():
    b = "a1   a2   a3"
    c = "b1   b2   b3"
    d = "c1   c2   c3"
    print(b)
    print(c)
    print(d)
    a1 = float(input("a1: "))
    a2 = float(input("a2: "))
    a3 = float(input("a3: "))
    b1 = float(input("b1: "))
    b2 = float(input("b2: "))
    b3 = float(input("b3: "))
    c1 = float(input("c1: "))
    c2 = float(input("c2: "))
    c3 = float(input("c3: "))
    g = a1 * (b2*c3 - b3*c2) - a2 * (b1*c3 - b3*c1) + a3 * (b1*c2 - b2*c1)
    print("value of determinant is:" , g)


import math
def sine():
    i = float(input("angle in radians: "))
    print(math.sin(i))

def cosine():
    i = float(input("angle in radians: "))
    print(math.cos(i))

def tangent():
    i = float(input("angle in radians: "))
    print(math.tan(i))

 