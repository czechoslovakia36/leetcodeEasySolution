class BikeRental:
    def __init__(self,stock=0):
        self.stock=stock

    def displayStock (self):
        print(f'We have currently {} bikes available to rent')
        return self.stock



bike1= BikeRental(5)
bike1.displayStock()
        
