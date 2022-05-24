# CLASS AND STATCIC METHODS

class Book:
    BOOK_TYPES=("HARDCOVER","PAPERBACK","EBOOK")

    # DOUBLE UNDERSCORE PROPERTIES ARE HIDDEN FROM OTHER CLASSES
    __booklist=None


    # class method works on class instance or class variables
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    @staticmethod
    def getbooklist():
        if Book.__booklist==None:
            Book.__booklist=[]
        else:
            return Book.__booklist




    def setTitle(self,newtitle):
        self.title=newtitle


    def __init__(self,title,booktype):
        self.title=title 

        if (booktype not in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype=booktype



# access the class attributes

print("Book types: ", Book.getbooktypes())
b1=Book("title1","HARDCOVER")
b2=Book("title 2","PAPERBACK")


thebooks= Book.getbooklist()

thebooks.append(b1)
thebooks.append(b2)

print(thebooks)

