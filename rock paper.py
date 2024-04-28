import random
scorey=0
scorec=0
opt=['rock','paper','scissor']
while True:
    x= random.choice(opt)
    y=int(input("""Enter your choice
1. Rock
2.Paper
3.Scissor
"""))
    if x== 'rock' and y ==1 :
        print(f"""Computer VS You
        {x} VS {opt[0]}""")
        print("Tie")
        cont=input("Do you wish to continue type y/n: ").lower()
        if cont=="y":
            continue
        else:
            break
    elif x== 'rock' and y ==2 :
        print(f"""Computer VS You
        {x} VS {opt[1]}""")
        print("You win")
        scorey+=1
        cont=input("Do you wish to continue type y/n: ").lower()
        if cont=="y":
            continue
        else:
            break
    elif x== 'rock' and y == 3 :
        print(f"""Computer VS You
        {x} VS {opt[2]}""")
        print("You loose")
        scorec+=1
        cont=input("Do you wish to continue type y/n: ").lower()
        if cont=="y":
            continue
        else:
            break
    elif x== 'paper' and y ==1 :
        print(f"""Computer VS You
        {x} VS {opt[0]}""")
        print("You loose")
        scorec+=1
        cont=input("Do you wish to continue type y/n: ").lower()
        if cont=="y":
            continue
        else:
            break
    elif x== 'paper' and y ==2 :
        print(f"""Computer VS You
        {x} VS {opt[1]}""")
        print("Tie")
        cont=input("Do you wish to continue type y/n: ").lower()
        if cont=="y":
            continue
        else:
            break
    elif x== 'paper' and y ==3 :
        print(f"""Computer VS You
        {x} VS {opt[2]}""")
        print("You win")
        scorey+=1
        cont=input("Do you wish to continue type y/n: ").lower()
        if cont=="y":
            continue
        else:
            break
    elif x== 'scissor' and y ==1 :
        print(f"""Computer VS You
        {x} VS {opt[0]}""")
        print("You win")
        scorey+=1
        cont=input("Do you wish to continue type y/n: ").lower()
        if cont=="y":
            continue
        else:
            break
    elif x== 'scissor' and y ==2 :
        print(f"""Computer VS You
        {x} VS {opt[1]}""")
        print("You loose")
        scorec+=1
        cont=input("Do you wish to continue type y/n: ").lower()
        if cont=="y":
            continue
        else:
            break
    elif x== 'scissor' and y ==3 :
        print(f"""Computer VS You
        {x} VS {opt[2]}""")
        print("Tie")
        cont=input("Do you wish to continue type y/n: ").lower()
        if cont=="y":
            continue
        else:
            break
    else:
        print("Choose a valid option(Type serial no. to choose)")
if scorey>scorec:
    print("You win. The score is: ",scorey,"-",scorec )
elif scorey<scorec:
    print("You loose. The score is: ",scorey,"-",scorec )
else:
    print("Tie. The score is: ",scorey,"-",scorec )