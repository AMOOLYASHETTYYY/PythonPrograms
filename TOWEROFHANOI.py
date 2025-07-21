def tower(disk,source,auxi,dest):
    if(disk==1):
        print("move disk 1 from {} to {}".format(source,dest))
        return
    else:
        tower(disk-1,source,dest,auxi)
        print("move disk {} from {} to {} ".format(disk,source,dest))
        tower(disk-1,auxi,dest,source)

disk=int(input("enter any number "))
print("steps involved arwe ")
tower(disk,'A','B','C')