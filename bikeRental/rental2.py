
import datetime
import math

class BikeRental:
    def __init__(self,stock=0):
        self.stock=stock

    def displayStock (self):
        print(f'We have currently {self.stock} bikes available to rent')
        return self.stock


    def rentBikeOnHourlyBasis(self,n):
        if n<=0:
            print("Number of bikes should be positive!")
            return None
        
        elif n > self.stock:
            print(f'Sorry! We have currently {self.stock} bikes available to rent')

        else:
            now=datetime.datetime.now()
            print(f'You have rented {n} bikes(s) on hourly basis today at {now}')
            print("You will be charged $5 for each hour per bike")
            print("We hope that you enjoy out service")

            self.stock-= n
            return now

    def rentBikeOnDailyBasis(self,n):

        if n<=0:

            print("Number of bikes should be positive!")
            return None
        
        elif n > self.stock:
            print(f'Sorry! We have currently {self.stock} bikes available to rent')

        else:
            now=datetime.datetime.now()
            print(f'You have rented {n} bikes(s) on hourly basis today at {now}')
            print("You will be charged $20 for each hour per bike")
            print("We hope that you enjoy out service")

            self.stock-= n
            return now

    def rentBikeOnDailyBasis(self,n):


        if n<=0:

            print("Number of bikes should be positive!")
            return None
        
        elif n > self.stock:
            print(f'Sorry! We have currently {self.stock} bikes available to rent')

        else:
            now=datetime.datetime.now()
            print(f'You have rented {n} bikes(s) on hourly basis today at {now}')
            print("You will be charged $60 for each hour per bike")
            print("We hope that you enjoy out service.")

            self.stock-= n
            return now   

    def returnBike(self,request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        Note: request is a tuple
        """
        rentalTime,rentalBasis,numOfBikes= request 
        bill=0

        # issue a bill only if all 3 param are not null!

        if rentalTime and rentalBasis and numOfBikes:
            self.stock+=numOfBikes
            now= datetime.datetime.now()
            rentalPeriod= now-rentalTime

            # hourly bill calculation
            
            if rentalBasis==1:
                bill = round(rentalPeriod.seconds/3600)*20*numOfBikes

            elif rentalBasis==3:
                # weekly
                bill= round(rentalPeriod.days/7)*60* numOfBikes

            elif rentalBasis==2:
                # daily bill calculation
                bill= round(rentalPeriod.days)*20 * numOfBikes


            if(3<= numOfBikes <=5):
                print("You are eligible for family rental promotion of 30% discount")
                bill=bill*0.7

            
            print("Thanks for returning your bike.Hope you enjoyed our service!")
            print(f"That would be ${bill}")
            return bill

        else:
            print("Are you sure you rented a bike with us?")
            return None


class Customer:
    def __init__(self):
        self.bike=0
        self.rentalBasic=0
        self.rentalTime=0
        self.bill=0

    def requestBike(self):
        bikes=input("How many bikes would you like to rent?")
        try:
            bikes=int(bikes)
        except ValueError:
            print("That's not a positive Integer!!")
            return -1
        if bikes < 1:
            print("Invalid Input. Number of bikes should be greater than zero!!")
            return -1
        else:
            self.bikes=bikes
        return self.bikes

def returnBike(self):
    if self.rentalBasis and self.rentalTime and self.bikes:
        return self.rentalTime, self.rentalBasic, self.bikes
    else:
        return 0,0,0





bike1= BikeRental(5)
bike1.rentBikeOnDailyBasis(2)
        
