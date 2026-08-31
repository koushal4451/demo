a = float(input("Enter your first number = "))
b = float(input("Enter your second number = "))

c = input("What do you want : ")

if c == "addition":
    print("The addition of two numbers is = ", a + b)
elif c == "subtraction":
    print("The subtraction of two numbers is = ", a - b)
elif c == "multiplication":
    print("The multiplication of two numbers is = ", a * b)
elif c == "division":
    print("The division of two numbers is = ", a / b)

print("Thank you for using this calculator")
