tempo = float(input("Digite o tempo gasto(em horas):"))
Velocidade = float(input("digite a velocidade media(em Km/h):"))

distancia = tempo*Velocidade
litros = distancia/12

print("velociade media:", Velocidade, "Km/h")
print("tempo gasto:", tempo, "em horas")
print("Distancia:", distancia, "Km")
print("quandiade de litros gastos:", '%.2f' %litros)