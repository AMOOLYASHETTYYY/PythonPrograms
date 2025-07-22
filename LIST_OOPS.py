class rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
       return(self.l*self.b)
list=[]
d=int(input("Enter no of objects"))
for i in range(d):
    r=rectangle(i+10,i+20)
    a=int((input("enter length ")))
    b=int(input("enter breadth "))

    list.append(r)
ind=0
for i in list:
    print("area of rectangle {} is {} ".format(ind+1,i.area()))
    ind=ind+1
