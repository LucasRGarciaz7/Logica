valor = float(input("Qual o valor da prestação?"))
tempo = int(input("Quanto tempo enta atrasado?"))

prestacao = valor + (valor*(2/100)*tempo)

print("O valor da prestação é:" '%.2F' %prestacao)