import random

'''
0 for gun
1 for snake
-1 for water
'''

computer = random.choice([1,-1,0])
youstr = input("Enter your choice : ")
youdict = {"s":1 , "w":-1 , "g": 0} 
reversedict = {1:"snake" , -1:"water" , 0 :"gun"}

you = youdict[youstr]


print(f"your choice {reversedict[you]} \n computer chouce {reversedict[computer]}")



if(computer==you):
        print("It is draw")
        

else:

    if(computer == -1 and you == 1):
            print(" You Win")
            
    elif(computer == -1 and you == 0):
            print(" You Lose")

    elif(computer == 1 and you == 0):
            print(" You Win")
            

    elif(computer == 1 and you == -1):
            print(" You Lose")
        
    elif (computer == 0 and you == -1):
            print(" You Win")
            
    elif(computer == 0 and you == 1):
            print(" You Lose")

    else:
            print("Something went Wrong")


