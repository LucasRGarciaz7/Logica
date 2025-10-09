nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))

media =(nota1 + nota2) /2
if media >= 6.0:
   print(f"voce ficou na media {media}")
else:
   exame = float(input("digite a nota do exame"))
   media =(nota1 + nota2 + exame) /3
   if media >= 5.0:
     print(f"voce passou no exame{media}")
   else:
      print(f"voce teve a capacidade de nao passar mesmo tendo exame {media}")
      


