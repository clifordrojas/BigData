
class Weed:

    def __init__(self, name,type,thc,price,brand, currency, producer):
        self.name = name
        self.type = type
        self.thc = thc
        self.price = price
        self.brand = brand
        self.currency = currency
        self.producer = producer

    def __str__(self):
        return self.name+"\t|"+ self.type +"\t|"+self.price +"\t|"+self.currency

    def toArray(self):
        return [self.name,self.price,self.brand]