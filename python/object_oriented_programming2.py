# ''' this is an example of single level inheretence  in which there is only one child and only one parent.'''
# # this is the parent class
# class person:
#     def setname(self, name):
#         self.name = name
#     def getname(self):
#         print(self.name)
    




# # this is the child class
# class student(person):
#     def setage(self, age):
#         self.age = age
#     def getage(self):
#         print(self.age)

# s1 = student()
# # so the class student is called for the object s1
# s1.setname("sahil")
# s1.setage(20)
# s1.getname()
# s1.getage()




''' the second type is multiple inheritence acc to which one child inherits from more than one parent classes.
    also the child class inherits the attributes as well as the methods from the parent(s) classes
    
    
    so the syntax is 
    class p1:
        methods
    class p2:
        methods
    class derived() 
'''
# like the child is inheriting some properties from his father and some from his mother and it doesn't have to be two parents.

# class car:
#     def setenginemodel(self, engine):
#         self.engine = engine
#     def getenginemodel(self):
#         print(self.engine)

# class tyre:
#     def settyrenumber(self, num):
#         self.num = num
#     def gettyrenumber(self):
#         print(self.num)

# class honda(car, tyre):
#     def setcarmodel(self, model):
#         self.model = model
#     def getcarmodel(self):
#         print(self.model)


# accord = honda()
# accord.setenginemodel('EK-1')
# accord.setcarmodel('v6')
# accord.settyrenumber(236)
# print('car details: ')
# accord.getcarmodel()
# accord.getenginemodel()
# accord.gettyrenumber()



''' multy level inheritence is different from multiple inheritence and here the inheritence goes in a straight line. '''
# class person:
#     def setname(self, name):
#         self.name = name
#     def getname(self):
#         print(self.name)

# class student(person):
#     def setage(self, age):
#         self.age = age
#     def getage(self):
#         print(self.age)

# class address(student):
#     def setaddress(self, address):
#         self.address = address
#     def getaddress(self):
#         print(self.address)


# # and the instance creation and the calling and assigning is left
''' and there is another type of inheritence called hybrid inheritence where both the multi level inheritence and the multiple inheritence are present together'''




# balls to the wall question and it is worth it. 
# and remember that only the method and the 
