class Calculator:
    
    # constructor
    def __init__(self , num1 , num2):
        self.num1 = num1
        self.num2 = num2


    # methods
    def Sum(self):
        print(f'{self.num1} + {self.num2} = ' , self.num1 + self.num2 )
        
    def Sub(self):
        print(f'{self.num1} - {self.num2} = ' , self.num1 - self.num2 )
    
    def mull(self):
        print(f'{self.num1} * {self.num2} = ' , self.num1 * self.num2 )
    
    def Div(self):
        print(f'{self.num1} / {self.num2} = ' , self.num1 / self.num2 )


# object
op = Calculator(10 , 2)
op.Sum()
op.Sub()
op.mull()
op.Div()