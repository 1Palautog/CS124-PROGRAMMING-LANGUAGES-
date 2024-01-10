def divide(x,y):
    if y==0:
        return "connot  divide by zero!"
    return x/y
while True:
    print("\n")
    num = float (input("First number: "))
    op= input ("Enter Operation +,-,*,/:")
    num2 = float (input("Second number: "))
    

    if op=='+':
        print(num, "+", num2, "=", num + num2)

    elif op=='-':
        print(num, "-", num2, "=", num - num2)

    elif op=='*':
        print(num, "*", num2, "=", num * num2)

    elif op=='/':
        print(num, "÷", num2, "=",divide (num, num2))
        
    else:
        print("invalid input")
    