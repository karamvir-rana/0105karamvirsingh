num1 = int(input("Enter First Number: "))
operation = int(input("Enter Operation: 1. add, 2. subtract, 3. multiply, 4. divide "))
num2 = int(input("Enter Second Number :"))
if operation == 1:
    print(num1+num2)
elif operation == 2:
    print(num1-num2)
elif operation == 3:
    print(num1*num2)
elif operation == 4:
    print(num1/num2)
else:
    print("Invalid Operator")
    

