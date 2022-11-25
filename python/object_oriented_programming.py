# # syntax
# class dog:
#     variable1
#     variable2
#     variable3
#     .
#     .
#     .
#     .
#     .
#     variableN

#     def __init__(self, arg1, arg2 ......, argn):

#     def method1(self, arg1, arg2, arg3, ......, argn):

#     def method2(self):

#     def methodn(self, arg1, arg2, arg3, ......, argn):

'''
class classname:
    # if there are some attributes then mention them else write pass
    student_1.name = 'sriram'
    student_2.age = 25
    # these are called instance variables which are not present in the class. 
    # so for the block of class
    # and the attributes that are mentioned in the class are common to the the class and the other variables are called the instance variables 
    # and they are unique to the object for the class.abs
    and the attributes are optional to a class that is it is not required .
    the __init__ thing means that initialise the things for the 
    
    the methods are the functions taht the objects may call for the sake of some thing.
    so self is the variable and the other parameters passed to the student will be the 
    and the init is a constructor. '''





class student:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
stud1 = student("sahil", 18, 'gautamsahil1947@gmail.com')
stud2 = student("ritik", 17, 'drskyritik@gmail.com')
print(stud1.age, stud1.email, stud1.name)
print(stud2.age, stud2.email, stud2.age)