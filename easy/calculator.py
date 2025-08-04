try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    operator = input("Enter operator:")
    if operator not in ["*","/","+","-"]:
        raise Exception("Invalid operator please enter *,/,-,+")
    result = None
    if operator == '*':
        result = num1*num2
    elif operator == '/':
        result = num1/num2
    elif operator == '-':
        result = num1-num2
    else:
        result = num1+num2
    print("Result is ",result)
except Exception as e:
    print(e)