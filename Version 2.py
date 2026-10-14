#Input
num1 = float(input("num1: "))

num2 = float(input("num2: "))

operation = int(input("1 = addition, 2 = subtraction, 3 = multiplication, 4 = division. Enter: "))

#functions
def add_numbers(num1, num2):
    return num1 + num2
    
def subtract_numebrs(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2
    
def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error: Cannot be defined"
    else:
        return num1 / num2

#Output
if operation == 1:
    print(add_numbers(num1,num2))
elif operation == 2:
    print(subtract_numebrs(num1,num2))
elif operation == 3:
    print(multiply_numbers(num1,num2))
elif operation == 4:
    print(divide_numbers(num1,num2))
else:
    print("Error: Try again")
    
