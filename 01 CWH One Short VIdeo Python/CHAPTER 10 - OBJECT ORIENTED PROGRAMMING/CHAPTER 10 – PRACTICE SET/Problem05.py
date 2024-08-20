# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways.

class Train:

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def bookTicket(self):
        if(self.seats > 0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry! This train is full now!")
            
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")

    def fareInfo(self):
        print("The price of the ticket is: ", self.fare)

obj = Train("Express 123", 90, 2)
obj.bookTicket()
obj.getStatus()
obj.fareInfo()  

obj.bookTicket()
obj.bookTicket()
obj.getStatus() 

obj.fareInfo()

         












