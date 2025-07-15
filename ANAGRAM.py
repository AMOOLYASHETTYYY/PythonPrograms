str1=input("enter the string1")
str2=input("enter the string2")
a=str1.lower()
b=str2.lower()
a1="".join(i for i in a if i !=" ")
b1="".join(i for i in b if  i !=" ")
news1=sorted(a1)
news2=sorted(b1)
if news1==news2:
    print("it is anagram")
else:
    print("not anagram")