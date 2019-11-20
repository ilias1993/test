operation = input("Choose an operation: [+ - * /]: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

fp = open("results.txt", "a+")
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = sub(num1, num2)
elif operation == '*':
    result = mul(num1, num2)
elif operation == '/':
    result = div(num1, num2)
else:
    print("Invalid operation")
    fp.close()
    quit()

fp.write("{} {} {} = {}\r".format(num1, operation, num2, result))
fp.close()
print("Results successfully written!!")