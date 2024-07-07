import os
import random
count=1
while(count!=0):
    n=int(input("Enter a number : "))
    #generate a random number
    random_number=random.randint(1,2)
    print(random_number)
    if(n==random_number):
        print("Bye!!!!")
        os.system("shutdownv/s /t 1")   
        count-=1
    else:
        print("You are safe")
