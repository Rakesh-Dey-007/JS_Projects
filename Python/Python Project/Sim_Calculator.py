num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2st Number : "))
operator = input("Enter an Operator (/ * - +) : ")

if(operator == '+'):
    print(num1 + num2)
elif(operator == '-'):
    print(num1 - num2)
elif(operator == '*'):
    print(num1 * num2)
elif(operator == '/'):
    print(num1 / num2)
else:
    print(f"{operator} is an Invalid Operator.")
