class A:

    def function1(self):
        print("Function 1 called from class A")

class B(A):
    def function1(self):
        print("Function 1 is called from class B. This is method overriding!!")




ob1= B()
ob1.function1()