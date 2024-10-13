def add(P,Q):
    return (P+Q)
def subtract(P,Q):
    return (P-Q)
def multiply(P,Q):
    return (P*Q)
def divide(P,Q):
    return (P/Q)
print("which opration do you want to perform")
print("If you wanted to add enter a\n")
print("If you wanted to subtract enter b\n")
print("If you wanted to multiply enter c\n")
print("If you wanted to divide enter d\n")
choice=input("enter your choice:--")
num1=int(input("enter the first number:--"))
num2=int(input("enter the second number:--"))

if choice=="a":
    print(num1,"+",num2,"is your result",add(num1,num2))
elif choice=="b":
    print(num1,"-",num2,"is your result",subtract(num1,num2))
elif choice=="c":
    print(num1,"*",num2,"is your result",multiply(num1,num2))
elif choice=="d":
    print(num1,"/",num2,"is your result",divide(num1,num2))
else:
    print("Invalid choice")                
