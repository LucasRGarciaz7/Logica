nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))
nota3 = float(input("digite a terceira nota:"))

media =(nota1 + nota2 + nota3) /3
if media >= 6.0:
   print("voce ficou na media" '%.2f' %(media))
else:
   print("voce nao passou" '%.2f' %(media))