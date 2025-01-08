class calculator:
    
    def __init__(self,num):
        self.num=num
        print(num)
        
    def square(self):
        print(f"The square is {self.num*self.num}")
        
    def cube(self):
        print(f"The cube is {self.num*self.num*self.num}")
        
    def squareRoot(self):
        print(f"The squareRoot is {self.num**1/2}")

myNum=int(input("Enter your number: "))
print(myNum)

a=calculator(myNum)
a.square()
a.cube()
a.squareRoot()