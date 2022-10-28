def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y==0:
        print('second number cannot be zero')
    else:
        return x / y
def Modulus(x, y):
    if y==0:
        print('second number cannot be zero')
    else:
        return x % y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")
n = 'Y'
while n == 'Y':
    s = input("Enter choice: ")
    if s in ('1', '2', '3', '4','5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except:
            print('enter valid input'.upper())
            continue
        if s == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif s == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif s == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif s == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif s == '5':
            print(num1, "%", num2, "=", modulus(num1, num2))
    else:
        print("Invalid Input")
    n=input('if you want to continue press Y\n'.upper())
    if n != 'Y':
        break
