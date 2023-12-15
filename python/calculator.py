choice = input("* - multiplication, / - division, + - addition , - - substraction: ")

a = int(input("First number: "))
b = int(input("Second number: "))

if choice == "+":
    print(a + b)
elif choice == "-":
    print(a - b)
elif choice == "*":
    print(a * b)
elif choice == "/":
    print(a / b)
    if (b == 0):
        print("you can't divide by 0")
    
        
