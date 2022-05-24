class Book:
    def __init__(self,title,author,pages,price):
        self.title=title
        self.author=author
        self.pages=pages
        self.price=price
        self.__secret="This is a secret attribute"
        # DOUBLE UNDERSCORE CAN PERVENT THE OVERRIDE
    
    def getprice(self):
        if hasattr(self,"_discount"):
            return self.price-(self.price*self._discount)
        else:
            return self.price

    def setdiscount(self,amount):
        self._discount=amount
        #  UNDERSCORE IS THE CONVENTION TO TELL US THAT IT IS A VARIABLE ONLY
        #  TO BE USED INSIDE CLASS

b1=Book("Brave new world","Leo tolstoy",1225,100)
b2=Book("war and peace","jd salinger",234,200)



# print(b1.getprice())
# b1.setdiscount(0.5)
# print(b1.getprice())
print(b1.__secret)
print(b1._Book__secret)


