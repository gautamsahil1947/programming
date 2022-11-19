'''
You are given subject-wise marks of the student which are stored in a tuple. Your task is to determine whether the student has "Passed" or "Failed".
Note:
• If the student has scored strictly below 35 in atleast three subjects, the student has failed otherwise confirm him/her as passed.
• Refer to the Displayed test cases for a beter understanding.
Constraints:
3 <= number of subjects <= 10
1 <= marks <= 100

input and output:
    input: 37,67,97,100,85
    output: Passed

'''
# solution

j = tuple(int(i) for i in input("input: ").split(","))

''' the line above takes input and splits it into a list (let it be m)
    the 'int(i) for i in' part iterates over the list m and returns the comma seprated integers
    and the tuple outside converts whatever inside into a tuple  '''
# print(j) can be used to check whether this worked or not
c = 0 # counting variable
for i in j:
    if (i < 35):
        c += 1
# the for block above iterates over the integers in the tuple
    # the if block compares the value and if it is less than 35, 1 is added to c
if (c >= 3):
    print("input: Failed")
else:
    print("output: Passed")
