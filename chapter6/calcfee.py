import math

class CalcFee:
    def __init__(self):
        self.shipping_fee = 1000
        self.tax_rate = 0.08
        self.value=0

    def calc(self):
        total = self.value + self.shipping_fee
        tax = math.ceil(total*self.tax_rate)
        v = math.ceil(total+tax)
        return v

    def addItem(self,price):
        self.value+=price

feel=CalcFee()
feel.addItem(500)
print(feel.calc(),"円")

fee2 = CalcFee()
fee2.shipping_fee=1500
fee2.addItem(800)
fee2.addItem(500)
print(fee2.calc(),"円")
