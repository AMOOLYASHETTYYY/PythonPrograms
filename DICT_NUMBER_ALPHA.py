dic={'A':1,'B':10,'C':100,'D':1000,'E':10000,'F':100000}
sum=0
ip="ABDC"
for i in ip:
    if i in dic:
        sum=sum+dic[i]
print(sum)
