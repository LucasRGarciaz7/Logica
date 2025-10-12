alturaP = float(input("digite a altura da parede:"))
larguraP = float(input("digite a largura da parede:"))
alturaA = float(input("digite a altura do azulejo:"))
larguraA = float(input("digite a largura do azulejo:"))

quantidadeA = (alturaP * larguraP) / (alturaA * larguraP)

print(f"quantidade de azulejos necessários:{quantidadeA}")