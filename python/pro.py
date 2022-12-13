class student():
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

n = int(input("enter the number of students: "))
for i in range(n):
    print("\r")
    print("\r") 
    print("\r")
    n = input("enter the name of the student " + str(i + 1) + " : ")
    a = int(input("enter the age of the student " + str(i + 1) + " : "))
    e = input("enter the email of the student " + str(i + 1) + " : ")
    std = student(n, a, e)
    print("\r")
    print("\r")
    print("\r")
    print("\r")
    print("the details of the student" + str(i + 1) + " are  : ")
    print("name : ", std.name)
    print("age : ", std.age)
    print("email : ", std.email)


