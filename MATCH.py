n=int(input("enter the no of teams"))
teams=[]
for i in range(n):
    t=input("enter the name")
    teams.append(t)
meet=int(input("enter the number of meetings"))
match=[]
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(meet):
            match.append([teams[i],teams[j]])
num=1
for i in match:
    print("{}. {} vs {} ".format(num,i[0],i[1]))
    num+=1


