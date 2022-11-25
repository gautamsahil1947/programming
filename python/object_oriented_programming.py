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





# class student:
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email
# stud1 = student("sahil", 18, 'gautamsahil1947@gmail.com')
# stud2 = student("ritik", 17, 'drskyritik@gmail.com')
# print(stud1.age, stud1.email, stud1.name)
# print(stud2.age, stud2.email, stud2.age)

# ''' the code above is very important.'''


''' and the thing is that mr sahil that you have to study otherwise it is not worth it.
    
    the object oriented programming is just normal programming but with modularity 
    an instance and an object is the same thing.

    the first parameter in the class method is called self and we do not pass any value for self
    and the __init__ constructor in the class is fired as soon as the class is called and the variables that the init
    has are called the local variables and those are local to the object

    and the object is also called an instance of the class.



'''



''' and there are 5 pillers of oops and one is inheretence.
    and if you have to make another class which wants to have some fratures from another class and 
    instead of copying the code from the other class is reused for the same purpose.
    
    
    and it says that there will be one parent class and one child class and this means that the child class will
    inherit all the properties from the parent class .
    
    
    let the parent class be A which is animal class.
    and other is the dog class.'''

class parent:
    attribute1 = 'hello'

    def method1():
        print("hello")

class child(parent):
    # this is the synatx for the parent child classes where the child class takes the advantage of the parent class
    pass