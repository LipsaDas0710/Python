import random

''' Snake:-1 ,Water:0 ,Gun:1'''

random_number = random.choice([-1, 0, 1])

computer=random_number
youEnter =input("Enter your choice: ")

Dict={"s":-1, "w":0, "g":1}
yourChoice=Dict[youEnter]

if(computer==yourChoice):
    print("It's a Draw!")
else:
    if(computer==-1 and yourChoice==0):
        print("You Win!")
    
    elif(computer==-1 and yourChoice==1):
        print("You Win!")
    
    elif(computer==0 and yourChoice==-1):
        print("You Lose!")
    
    elif(computer==0 and yourChoice==1):
        print("You Win!")
    
    elif(computer==1 and yourChoice==0):
        print("You Lose!")
    
    else:
        print("You Lose!")
    