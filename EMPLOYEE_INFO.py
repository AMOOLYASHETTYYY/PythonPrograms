class emp:
    profit=1000000
    tax=10
    company="cognizant"
    def __init__(self,name,age,sal,per):
        self.name=name
        self.age=age
        self.sal=sal
        self.per=per

    def cal_tax(self):
        return((emp.tax/100)*self.sal)

    def cal_share(self):
        return((self.per/100)*emp.profit)
    def display(self):
        print("1.",self.name)
        print("2.",self.age)
        print("3.",emp.company)
        print("4.",self.sal)
        print("5.",self.cal_tax())
        print("6.",self.cal_share())
a1=emp("amoolya",20,600000,10)

a1.display()