b=input("enter the boys name ")
g=input("enter the girls name ")
boy=list(b)
girl=list(g)
for i in range(len(boy)):
    for j in range(len(girl)):
        if boy[i]==girl[j]:
            boy[i]='2'
            girl[j]='2'
for i in boy:
    if i=='2':
        boy.remove(i)
for i in girl:
    if i=='2':
        girl.remove(i)
num=len(boy)+len(girl)
print(num)
ans=['F','L','A','M','E','S']
ind=0
while(len(ans)!=1):
    ind=(ind+(num-1))%len(ans)
    ans.pop(ind)
print("The relation is ",ans)

