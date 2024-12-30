import math

last_result = None

def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b==0:
        print("Error: Division by zero is not allowed")
        return None
    return a / b
def exponentiate(a,b):
    return a**b

def square_root(a):
    if a<0:
        print("Error: Cannot compute square root of negative number.")
        return None
    return math.sqrt(a)
def sin_function(a):
    return math.sin(math.radians(a))

def cos_function(a):
    return math.cos(math.radians(a))
def tan_function(a):
    return math.tan(math.radians(a))

def show_menu():
    print("\nChoose an operation:")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")
    print("10. Recall last result")
    print("11. Exit")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
def perform_calculation():
    global last_result
    while True:
        show_menu()
        choice = input("Enter the number for operation:")

        if choice == '1':
            num1 = get_number("Enter the first number:")
            num2 = get_number("Enter the second number:")
            last_result = add(num1,num2)
            print(f"Result:{last_result}")

        elif choice =='2':
            num1 = get_number("Enter the first number:")
            num2 = get_number("Enter the second number:")
            last_result=substract(num1,num2)
            print(f"Result:{last_result}")

        elif choice =='3':
            num1 = get_number("Enter the first number:")
            num2 = get_number("Enter the second number:")
            last_result = multiply(num1,num2)
            print(f"Result:{last_result}")

        elif choice == '4':
            num1 = get_number("Enter the first number:")
            num2 = get_number("Enter the second number:")
            last_result = division(num1,num2)
            if last_result is not None:
                print(f"Result:{last_result}")

        elif choice == '5':
            num1 = get_number("Enter the base number:")
            num2 = get_number("Enter the exponenet number:")
            last_result = exponentiate(num1, num2)
            print(f"Result: {last_result}")

        elif choice == '6':
            num = get_number("Enter the number to find square root:")
            last_result = square_root(num)
            if last_result is not None:
                print(f"Result: {last_result}")

        elif choice == '7':
            angle = get_number("Enter the angle in degrees:")
            last_result = sin_function(angle)
            print(f"Result : {last_result}")

        elif choice == '8':
            angle = get_number("Enter the angle in degrees:")
            last_result = cos_function(angle)
            print(f"Result : {last_result}")

        elif choice == '9':
            angle = get_number("Enter the angle in degrees:")
            last_result = tan_function(angle)
            print(f"Result:{last_result}")

        elif choice == '10':
            if last_result is not None:
                print(f"Last result:{last_result}")
            else:
                print("No previous result to recall.")

        elif choice == '11':
            print("Thank you")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":

    perform_calculation()

        
         
        
            
    



