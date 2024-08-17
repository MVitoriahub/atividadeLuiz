def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios,custo_pedagio):  # função para cálculo do custo de viagem
    custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel  # calcula o combustivel total
    custo_pedagio_total = numero_pedagios * custo_pedagio  # calcula o total de pedagio
    custo_total = custo_combustivel_total + custo_pedagio_total  # calcula o custo total
    return custo_total, custo_combustivel_total, custo_pedagio_total  # retorna os cálculos acima
distancia = float(input("Digite a distância da viagem (em km): "))  # lê a distância
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): "))  # lê o combustível
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): "))  # lê o consumo do veículo
numero_pedagios = int(input("Digite o número de pedágios no percurso: "))  # lê o número de pedágios
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): "))  # lê o custo do pedágio
custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia,custo_combustivel,consumo_veiculo, numero_pedagios,custo_pedagio)  # equivale as funçao

print(f"Custo total da viagem: R${custo_total:.2f}")  # imprime o custo total da viagem
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}")  # imprime o custo total do combustível
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}")  # imprime o custo total do pedágio
