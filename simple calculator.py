num1=float(input("enter first number:"))
op=input("enter operators(+,-,*,/):")
num2=float(input("enter second number:"))
if op=='+':
    result=num1+num2
elif op=='-':
    result=num1-num2
elif op=='*':
    result=num1*num2
elif op=='/':
    result=num1/num2
else:
    result="invalid operator"
print(f"result is{result}")
