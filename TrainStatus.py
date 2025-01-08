from random import randint
class TrainStatus:
    def __init__(self, trainNo):
        self.trainNo=trainNo
    
    def book(self,fro,to):
        print(f"Ticket is booked in train no. {self.trainNo} from {fro} to {to}.")
        
    def getStatus(self):
        print(f"Train no.: {self.trainNo} is running on time.")
        
    def getFare(self,fro,to):
        print(f"Ticket fare in train no. {self.trainNo} from {fro} to {to} is {randint(222,3333)}.")
        
myTrain=int(input("Enter your Train no.: "))
a=TrainStatus(myTrain)
a.book("Delhi","Jaipur")
a.getStatus()
a.getFare("Delhi","Jaipur")