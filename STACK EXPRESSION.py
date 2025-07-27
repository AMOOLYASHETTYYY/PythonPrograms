def find(exp):
    op=[]
    opnd=[]
    p={'+':2,'-':2,'*':3,'/':3}
    i=0
    while(i<len(exp)):
        if exp[i].isdigit():
            num = ""
            while(i<len(exp) and exp[i].isdigit()):

                num=num+exp[i]
                i=i+1
            opnd.append(int(num))
        else:
            while(op and p[op[-1]]>=p[exp[i]]):
                o=op.pop()
                num2=opnd.pop()
                num1=opnd.pop()
                if o=='+':
                    opnd.append(num1+num2)
                elif o=='-':
                    opnd.append(num1 - num2)
                elif o=='*':
                    opnd.append(num1 * num2)
                elif o=='/':
                    opnd.append(num1//num2)
            op.append(exp[i])
            i=i+1
    while(op):
        o = op.pop()
        num2 = opnd.pop()
        num1 = opnd.pop()
        if o == '+':
            opnd.append(num1 + num2)
        elif o == '-':
            opnd.append(num1 - num2)
        elif o == '*':
            opnd.append(num1 * num2)
        elif o == '/':
            opnd.append(num1 // num2)

    return opnd[0]




exp="10+2*3/4+3"
res=find(exp)
print(res)
