class CalculateSalary:
    def __init__(self, dailyWage, workdays ):
        self.workdays = workdays
        self.dailyWage = dailyWage
        self.gross = 0
        self.net = 0
        self.totalGross();
        self.taxCuttings()

    def totalGross(self):
        self.gross = self.dailyWage * self.workdays
    
    def taxCuttings (self):
        self.net = self.gross - ((self.gross * 7) / 100) 
        
    def printTotal(self):
        print("Total Salary after taxes  : ")
        print(  self.net );
    

jhon = CalculateSalary(900,28)
jhon.printTotal()
print("This is functional cohesion because all the function related to salary calculations are added here ")