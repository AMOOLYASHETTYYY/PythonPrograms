a=input("enter the password")
up=0
lw=0
sp=0
dg=0
if len(a)>7:
    for i in a:
        if i.isupper():
            up+=1
        elif i.islower():
            lw+=1
        elif i.isdigit():
            dg+=1
        else:
            sp+=1

    if up>0 and lw>0 and sp>0 and dg>0:
        print("Good password")
    else:
        print("bad password")
else:
    print("password needs to be atleast 8 characters")
