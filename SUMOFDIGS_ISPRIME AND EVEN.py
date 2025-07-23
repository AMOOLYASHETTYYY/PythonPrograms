class A:
    def isprime(self,a):
        self.a=a
        for i in range(2,self.a):
            if self.a%i==0:
                return False
        return True
class B:
    def sod(self,a):
        self.a=a
        return sum([int (i) for i in str(self.a)])
class C(A,B):
    def show(self):
        print("hello")
s1=A()
print(s1.isprime(20))
s2=B()

s3=C()
s3.show()
print(s3.isprime(30))
print(s3.sod(110))
