"""class father:
    car="BWM"
    money=500000
    def wealth(self):
        print(" money is =",self.money)
        print(" caris =",self.car)
class son(father):
    pass

f=father()
f.wealth()
print("----")
s=son()
s.wealth()"""

"""class big_bro:
    def __init__(self):
        self.car="BMW"
        self.phone="vivo"
        self.bike="xstream"
    def wealth(self):
        print("big_bro car is=",self.car)
        print("big_bro phone is=",self.phone)
        print("big_bro bike is=",self.bike)
class young_bro(big_bro):
    def __init__(self):
        self.car="XXX"
        self.phone="samsang"
        self.bike="yyy"
    def wealth(self):
        print("younger_bro car is=",self.car)
        print("younger_bro phone is=",self.phone)
        print("younger_bro bike is=",self.bike)
    
#b=big_bro()
#b.wealth()
print("------")
y=young_bro()
y.wealth()"""


"""class big_bro:
    def __init__(self):
        self.car="BMW"
        self.phone="vivo"
        self.bike="xstream"
    def wealth(self):
        print("big_bro car is=",self.car)
        print("big_bro phone is=",self.phone)
        print("big_bro bike is=",self.bike)
class young_bro(big_bro):
    def __init__(self):
        super().__init__(phone,car,bike)
        super().wealth()
        self.car="XXX"
        self.phone="samsang"
        self.bike="yyy"
    def wealth(self):
        print("younger_bro car is=",self.car)
        print("younger_bro phone is=",self.phone)
        print("younger_bro bike is=",self.bike)
    
#b=big_bro()
#b.wealth()
print("------")
y=young_bro()
y.wealth()"""

class online_shopping:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print("laptop is =",self.name)
        print("price is=",self.price)
class tax_percentage(online_shopping):
    def __init__(self,name,price,tax):
        super().__init__(name,price)
        self.tax=tax
    def total_price(self):
        print("total price",self.price+(self.price*self.tax/100))
t=tax_percentage("laptop",50000,18)
t.display()
t.total_price()




        



        
