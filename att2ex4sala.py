a = float(input("digite o lado A do triangulo:"))
b = float(input("digite o lado B do triangulo:"))
c = float(input("digite o lado C do triangulo:"))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("equilatero")
    elif a == b or a == c or b == c:
        print("isosceles")
    else:
        print("escaleno")
else:
    print("os lados nao formam um triangulo")

