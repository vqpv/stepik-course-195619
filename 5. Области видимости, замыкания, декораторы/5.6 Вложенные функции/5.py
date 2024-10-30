def calculate(x, y, operation="a"):
    def addition(a, b):
        return a + b
    
    def subtraction(a, b):
        return a - b
    
    def division(a, b):
        if b != 0:
            return a / b
        else:
            return "На ноль делить нельзя!"
    
    def multiplication(a, b):
        return a * b
    
    if operation == "a":
        print(addition(x, y))
    elif operation == "s":
        print(subtraction(x, y))
    elif operation == "d":
        print(division(x, y))
    elif operation == "m":
        print(multiplication(x, y))
    else:
        print("Ошибка. Данной операции не существует")
