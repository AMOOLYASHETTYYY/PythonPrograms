str1=input("enter the string")
c=0
for i in range(len(str1)):
    if (str1[i]==" " and str1[i+1]!=" "):
        c=c+1
print("no of words is ",c+1)