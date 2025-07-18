def gcd(a,b):
    while(b!=0):
        temp=a%b
        a=b
        b=temp
    return a

def cop(a,b):
    return gcd(a,b)==1



n=int(input("enter the range "))
for i in range(n):
    for j in range(1,i):
        for k in range(1,j):
            if (k*k+j*j==i*i and cop(i,j) and cop(j,k)):
                print(k,j,i)






