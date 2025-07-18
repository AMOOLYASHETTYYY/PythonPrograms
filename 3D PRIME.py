

def isprime(i):
    if(i==1):
        return False
    else:
        for j in range(2,i):
            if(i%j==0):
                return False
            return True


def digprime(i):
    while(i>0):
        d = list(str(i))
        x = sum([int(i) for i in d])





def sumprime(i):
    d=list((str(i)))
    x=sum([int(i) for i in d ])
    if(isprime(x)):
        return True
    else:
        return False


for i in range(100,1000):
    if isprime(i) and digprime(i) and sumprime(i):
        print(f"the number {i} is a 3d prime ")









