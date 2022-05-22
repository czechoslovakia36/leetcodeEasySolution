class car:
    def __init__(self,name=None,year=None):
        self.name=name
        self.year=year

    def __str__(self):
        return f' name:{self.name} \n year:{self.year}'


car0= car("bmw","2020")
print(car0.__str__)

print(car0)
