import math

a = float(input("digite o valor de a"))
b = float(input("digite o valor de b"))
c = float(input("digite o valor de c"))

delta = b**2- 4*a*c

if delta <0:
    print("nao a raizes reais")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"raizes reais e iguais {raiz}")
else:
    raiz1 = (-b+math.sqrt(delta))/2*a
    raiz2 = (-b-math.sqrt(delta))/2*a
    print(f"as raizes sao r1={raiz1}; r2={raiz2}")