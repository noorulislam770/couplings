class Car:
    def __init__(self, model, vendor):
        self.model = model
        self.vendor = vendor
    
    def drive(self):
        print("Woooo Wooo");

    def details(self):
        print("Model "+ self.model+  " of " + self.vendor)


def displayCarModel(car):
    print("car Model is +> " + car.model)



Toyota = Car("corola", "toyota")
displayCarModel(Toyota)


print("this is an example of stamp coupling as we send all the car object insetead of just the model ")