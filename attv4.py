var1 = int(input("Digite o valor da primeira variavel:"))
var2 = int(input("Digite o valor da segunda variavel:"))

C = var1
var1 = var2
var2 = C

print("O valor trocado é de A =", '%.2F' %var1, "e B =",'%.2F' %var2)