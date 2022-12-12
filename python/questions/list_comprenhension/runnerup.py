''' Given the participants score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
    stdin: 
    5
    20 25 6 6 14
    stdout:
    20
'''

''' method 1 
    take the inputs and split the second input
    append the terms which are not equal to the max term to an empty list
    and print the max term form that appended list.
'''
'''
n = int(input())
scores = list(map(int, input().split(" ")))
emptylist = []
maxscore = max(scores)
for i in scores:
    if (i != maxscore):
        emptylist.append(i)
print(max(emptylist))
'''


'''

# this is another solution
n = int(input())
scores = list(map(int, input().split(" ")))
scores.sort()
scores = set(scores)
scores = list(scores)
if (len(scores) >= 2):
    print(scores[-2])
else:
    print(scores[-1])

'''



