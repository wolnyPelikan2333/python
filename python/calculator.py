wybor = input("* - mnożenie, / -dzielenie, + -dodawanie, - -odejmowanie: ")

a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))

if wybor == "+":
    print(a + b)
elif wybor == "-":
    print(a - b)
elif wybor == "*":
    print(a * b)
elif wybor == "/":
    print(a / b)
    if (b == 0):
        print("nie możesz dzielić przez 0")
    
        
