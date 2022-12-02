# file handeling
''' 
two types of files
    text files
    binary files
a file has two main parts the file name and the file extension
the extension for a text file is .txt
there is a concept called pickling in case of binary files.
    functions taht are used while working with a file
        open the file
        read the file
        write the file
        append the file
        update the file
        rename the file
        close the file
the syntax to open a file is 
    f = open(filename, mode(optional))
        various modes for a file
            r = read
            w = write
            a = append
            rb = read binary file
            wb = write the binary file
            x = exclusive
        and by default if not mentioned the mode is read
        and the file should be in the same location as the ide file for not errorless execution. '''

'''
# how to read a file

file = open ("hello.txt", 'r')
for f in file:
    print(f)


and it is a good practice for you to close the file with 
    file.close()
and it frees up the storage 


and also if you didn't create a file then the programm will show an error 
and this error will be only in the read mode and not in write mode and the append mode 
and in the write mode it will create a new file for that name

and if a file is encrypted then it will show error message similar to excess denied. '''

''' and there is anoter method to read the file
    instead of using the for loop you can use the file.read() '''

'''
file = open('hello.txt', 'r')
print(file.read()) '''

'''
f = open ('hello.txt', 'w')
f.write('abc') '''
# the code above writes the characters to the file and if the file does not exist then it will create a new file with these contents


f = open ('hello.txt', 'a')
f.write('this is the appended text')
f.close()


''' hi note that there is no attribute called append to a file and the main thing is that if you mention
    append as the opening mode then the written text or the written stuff is added at the end of the previous content


        file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London"]
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("myfile.txt", "a") # append mode
file1.write("Today \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()

# Write-Overwrites
file1 = open("myfile.txt", "w") # write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(file1.read())
print()
file1.close()

    this is the code from geeks for geeks and all the things are well illusttrated here.
'''

''' read is to read the content of the fiile
    tell is to tell the position of the cursor in the file
    seek will take the cursor to the location you want
    readline()
    close
    write
'''

''' the r+ mode means read and write.
    '''
''' waht is pickling
        whenever you are using any obj in python 
            pickling is used to preserve the data structure 
                serialisation and deserialisation
                this is related to the sequence of the list or the tuple
                and there is another term called unpickeling 
                    load and dump functions
            to use pickling you have to import pickle module 
            and it has load() and dump()  
            load is just like reading the file and dump is like writing a file
        benifits to pickling
            it secures the data, and with the advantages there are disadvantages and do not unpickle files from an untrusted sourse
            and also try to know how the data is protected in a binary file in this process.

'''













