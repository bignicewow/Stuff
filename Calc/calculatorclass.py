class Calculator:
    def __init__(self):
        
        self.result = 0

    def add(self, number):
        self.result += number
    
    def subtract(self, number):
        self.result -= number
    
    def multiply(self, number):
        self.result *= number

    def divide(self, number):
        self.result /= number
    

if __name__ == "__main__":
    calculator = Calculator()
    calculator.add(5)
    calculator.multiply(2)
    calculator.add(100)
    calculator.subtract(10)
    calculator.divide(20)
    print(calculator.result)