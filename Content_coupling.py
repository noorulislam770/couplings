class Car:
    def __init__(self, model, vendor):
        self.model = model
        self.vendor = vendor
        self.engine = Engine(25,"Toyota")
    
    def drive(self):
        print("Woooo Wooo");

    def details(self):
        print("Model "+ self.model+  " of " + self.vendor + " Engine From " + self.engine.vendor)


    
    def changeEngine(self, newcc, newVendor):
        self.engine.cc = newcc
        self.engine.vendor = newVendor


class Engine:
    def __init__(self,cc,vendor):
        self.cc = cc
        self.vendor = vendor

    def start(self):
        print("starting engine")

car = Car ('model Y', "tesla")

car.details();
car.changeEngine("900", "mercedes")
car.details()

print("Content Coupling as the car Class Changed the engine class variables inside it self with calling proper mehtods")