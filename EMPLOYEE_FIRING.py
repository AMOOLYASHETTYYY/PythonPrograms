names=["A","B","C","D","E","F","G","H","I","J"]
memo=[0,1,1,1,2,2,1,2,1,2]
sal=[1000,2000,3000,4500,2000,5000,1500,2300,1300,1100]
removed=[]

data=list(zip(names,memo,sal))
for i in data:
    if (i[2]>4000):
        removed.append(i)

remaining=[i for i in data if i[2]<4000]
a=sorted(remaining,key=lambda x:x[2],reverse=True)
print(a)
removed2=[]
for i in a:
    if i[1]>=2:
        removed.append(i)
    if len(removed2)>3:
        break
final=removed+removed2
ind=1
for i in final:
    print("{}.{} : Memo {} : salary {} ".format(ind,i[0],i[1],i[2]))
    ind+=1


