n = list(map(str,input("Enter the equation seperated by space ex: 45 * 84: ").split()))
if n[1]=='+':
    print(*n,'=',float(n[0]) + float(n[2]))
elif n[1]=='-':
    print(*n,'=',float(n[0]) - float(n[2]))
elif n[1]=='*':
    print(*n,'=',float(n[0]) * float(n[2]))
elif n[1]=='/':
    print(*n,'=',float(n[0]) / float(n[2]))
else:
    print("enter valid operator i.e. '+,-,*,/'")