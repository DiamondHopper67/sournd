class Car:
    def __init__(self, model, color, speed, company):
        self.model = model
        self.color = color
        self.speed = speed
        self.company = company
    def start(self):
        print("Car has started")
    def accelerate(self, value):
        print("Car acceleration is ",value)

car1 = Car("A1", "red", 70, "tesla")
print(car1.speed)
car1.start()
car1.accelerate(30)

class Atm:
    def __init__(self,pin, cardnumber):
        self.pin = pin
        self.cardnumber = cardnumber
    def balence(self):
        print("you have no money in account")
    def credit(self,money):
        print("value", money)

atm1=Atm(1234,1234567890)
print(atm1.cardnumber)
atm1.balence()
atm1.credit(1)