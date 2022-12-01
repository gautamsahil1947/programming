# pseudocode
''' take input number from the user
        print tables from 2 till taht number'''
class tables:
    # creating a method
    def gettables(self, i):
        self.i = i
        # loops for the tables.
        for j in range(2, self.i + 1):
            for k in range(1, 11):
                print(j, "x", k, "=", (j*k))
            print("\r")


while (True):
    # this is the number till which we are suppose to print the tables
    n = int(input("Enter a positive number : "))
    if (n >= 2):
        # creating an instance
        obj = tables()
        # calling the method
        obj.gettables(n)
        break
    else:
        continue
