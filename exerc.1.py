def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso):#função para calcular
    taxa_juros_diaria = taxa_juros_anual / 365 / 100 #calcula a taxa de juros diaria, para isso, é dividida taxa_juros_anual pelo numero de dias do ano por 100(%)

    juros = valor_principal * taxa_juros_diaria * dias_atraso#calcula a taxa de juros total

    valor_total = valor_principal + juros# calcula o valor total, para isso soma o valor do item, adicionado dos juros total
    return valor_total, juros # retorna o valor total, bem como os juros

    valor_principal = 1000.00#informa o valor do item
    taxa_juros_anual = 5.0#informa a taxa de juros/
    dias_atraso = 30#informa os dias de atraso
    valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)#chama a função e passa os parâmetros.
    print(f"Valor total a ser pago: R${valor_total:.2f}")#imprime o valor total a ser pago
    print(f"Valor dos juros: R${juros:.2f}")#imprime o valor dos juros