a=int(input("enter the number of blocks:"))
b=int(input("enter the number of lines:"))
c=int(input("enter the number of stars:"))
sum=0
count=0
print("--------------")
for i in range(a):
    print(f"---------{i+3}---------")
    count=0
    for j in range(b-i):
        for k in range(c):
            print("*",end="")
            count+=1
        print()
    print(count)
    sum+=count
print(sum)

