class Car:
    def __init__(self, model, vendor):
        self.model = model
        self.vendor = vendor
    
    def drive(self):
        print("Woooo Wooo");

    def details(self):
        print("Model "+ self.model+  " of " + self.vendor)



def displayCarmodel(model):
    print("car Model is +> " + model)


print("this is an example of data coupling as we send just the model of the car  ")