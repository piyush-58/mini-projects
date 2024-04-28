import random as rm
def start():
    n = int(input("enter start of the range: "))
    n1= int(input("enter end of the range: "))
    x= rm.randrange(n,n1)
    return x
y=start()
while True:
    guess= int(input("Guess a number"))
    if(guess==y):
        print("You have guessed the correct no.")
        cont=input("Do you wish to continue type y/n: ").lower()
        if cont!="y":
            break
        else:
            y=start()
    elif(guess>y):
        print("Your guess is higher then the number")
    else:
        print("Your guess is lower then the number")