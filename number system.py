n1=int(input('enter the start of the range: '))
n2=int(input('enter the end of the range(not including this number): '))
n4=int(input('enter updation value'))
if n2>n1:
    n3= int(input("""-----Choose the order (Type serial no. to choose)-----
    1. Ascending
    2. Descending
    3. row-wise
    4. column-wise
    """))
    if n3==1 or n3==4:
        for i in range(n1,n2,n4):
            print(i)
    elif n3==2:
        for i in range(n2-1,n1-1,-n4):
            print(i)
    elif n3==3:
        for i in range(n1,n2,n4):
            print(i,end=' ')
    else:
        print("Choose a valid order(Type serial no. to choose)")
else:
    print("end of range should be higher than the start of it")
