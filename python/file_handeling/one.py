''' open a text file named input data 1 in read mode and then open output data file 
    in write mode. copy the contents of the input file in the second file and then close both the files'''


f = open("data1.txt", 'r')
# opened a file in read mode.
h = open('hi.txt', 'w')
for i in f:
    h.write(i)
f.close()
h.close()
# do not froget to close the file at the end..

