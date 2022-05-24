class Book:
    def __init__(self,title):
        self.title=title

class Newspaper:
    def __init__(self,name):
        self.name=name



b1=Book("The catcher in the rye")
b2=Book("the grapes of wrath")

n1=Newspaper("The washington post")
n2=Newspaper("The new tork times")


print(type(b1)==type(b2))
# or
print(isinstance(b1,Book))
print(isinstance(n2,object))

# object is built. all classes are derived from object

# print(isinstance(2,object))