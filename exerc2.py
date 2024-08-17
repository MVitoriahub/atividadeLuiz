def calcular_area_comodos():# calcula a area dos comodos
    total_area = 0#considera a area total com valor nulo


    while True:#estabelece uma estrutura de repetição, ou seja, enquanto for verdadeiro, ela se repetirá

      largura = float(input("Digite a largura do cômodo (em metros): "))#faz a leitura da largura
      comprimento = float(input("Digite o comprimento do cômodo (em metros): "))#faz a leitura do comprimento

      area_comodo = largura * comprimento#calcula a area do comodo, usando para isso as informações recebidas da largura e do comprimento
      print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.")#imprime a area total do comodo

      total_area += area_comodo#adiciona, no valor da área total, a área do cômodo calculada anteriormente

      mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()#pergunta ao usuário se deseja adicionar mais cômodos e, em seguida, lê a resposta
      if mais_comodos != 's':#se a resposta for diferente de sim, a estrutura de repetição é pausada e é retornado o valor total da área
        break

    return total_area

area_total = calcular_area_comodos()#chama a função para o cálculo da área dos cômodos, dizendo que seu valor é equivalente a área total
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")#é impressa a área total
