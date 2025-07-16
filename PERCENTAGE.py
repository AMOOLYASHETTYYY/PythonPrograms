names=[]
marks=[]
percentage=[]
total=0
for i in range(2):
    a=input("enter the name ")
    names.append(a)
    students=[]
    for j in range(3):
        sub=int(input(f"enter marks sub {j+1}"))
        students.append(sub)
    marks.append(students)


for i in marks:
    res=sum(i)//3
    percentage.append(res)



for i in range(2):
    print("{}.{} : {}%".format(i+1,names[i],percentage[i]))
