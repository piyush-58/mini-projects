import random
scorey=0
scorec=0
while True:
    x= random.randrange(1,7)
    y= random.randrange(1,7)
    print("you got:",y,"AND","engine got:",x)
    scorey+=y
    scorec+=x
    cont=input("Do you wish to continue type y/n: ").lower()
    if cont=="y":
        continue
    else:
        break
if scorey>scorec:
    print("You win. The score is: ",scorey,"-",scorec )
elif scorey<scorec:
    print("You loose. The score is: ",scorey,"-",scorec )
else:
    print("Tie. The score is: ",scorey,"-",scorec) 