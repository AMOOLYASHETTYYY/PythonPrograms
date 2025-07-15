
heads = int(input("Enter total number of heads: "))
legs = int(input("Enter total number of legs: "))
flag=False
for hens in range(heads):
    cow=heads-hens
    if(cow*4 + hens*2==legs):
        print("cows:",cow)
        print("hens:",hens)
        flag=True
        break
if(not flag):
    print("no solution")
