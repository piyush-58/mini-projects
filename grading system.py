f = open("test.txt","w+")
print("----Welcome to Student's Database----")
rec={}
while True:
    n1=int(input("""Enter your choice(Type serial no. to choose)
1. Add
2. Modify
3. Search
4. Delete
"""))
    if n1==1:
        n2 = eval(input("enter the record in dictionary format:{'student name':age} "))
        rec = rec | n2
        print(rec)
        cont=input("Do you wish to continue type y/n: ").lower()
        if cont!="y":
            break
    elif n1 == 2:
        print("which key-value pair do you wish to modify?")
        print(rec)
        n3 = input("Type the key: ")
        n4 = int(input("type the value: "))
        if n3 not in rec:
            print("enter a valid key: ")
        else:
            rec[n3]=n4
            print(rec)
        cont=input("Do you wish to continue type y/n: ").lower()
        if cont!="y":
            break
    elif n1 == 3:
        n5=input("Type the Key to search for it: ")
        if n5 in rec:
            print(n5,":",rec[n5])
        else:
            print(n5,"not found in the database")
        cont=input("Do you wish to continue type y/n: ").lower()
        if cont!="y":
            break
    elif n1 == 4:
        n6=input("Type the Key you wish to delete: ")
        if n6 in rec:
            rec.pop(n6)
            print(rec)
        else:
            print(n6,"not found in the database")
        cont=input("Do you wish to continue type y/n: ").lower()
        if cont!="y":
            break
        else:
            print("Choose a valid option(Type serial no. to choose)")