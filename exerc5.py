def calcular_imc(peso, altura):#funçã para calcular Imc, usando peso e altura
    imc = peso / (altura ** 2)#formula do IMC
    return imc#retona o valor do Imc


def classificar_imc(imc):#função para classificar IMC


    if imc < 18.5:#estrutura condicional
        return "Abaixo do peso"#caso esteja abaixo de 18.5, retorna a mensagem
    elif 18.5 <= imc < 24.9:#caso esteja acima de 18.5 e abaixo de 24.9, retorna a mensagem
        return "Peso normal"
    elif 25 <= imc < 29.9:#caso esteja acima 25 e abaixo de 29.9, retorna a mensagem
        return "Sobrepeso"
    elif 30 <= imc < 34.9:#caso esteja acima de 30 e abaixo de 34.9, retorna a mensagem
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:#caso esteja acima de 35 e abaixo de 39.9, retorna a mensagem
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"# do cntrário, é retornado essa mensagem


def sugestao_atividade_fisica(classificacao_imc):#função que usa dados da função acima
    if classificacao_imc == "Abaixo do peso":#estrutura de condicional
        return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em proteínas e calorias."   #retornada essa mensagem
    elif classificacao_imc == "Peso normal":
        return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e natação, junto a um treino de força moderado."   #retornada essa mensagem
    elif classificacao_imc == "Sobrepeso":
        return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além de exercícios de resistência." #retornada essa mensagem
    elif classificacao_imc == "Obesidade grau 1":
        return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um programa de reeducação alimentar."    #retornada essa mensagem
    elif classificacao_imc == "Obesidade grau 2":
        return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e acompanhamento nutricional."     #retornada essa mensagem
    else:
         "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica, fisioterapia, e consultas regulares com um nutricionista." #retornada essa mensagem

peso = float(input("Digite seu peso (em kg): "))#leitura do peso
altura = float(input("Digite sua altura (em metros): "))#leitura da altura
imc = calcular_imc(peso, altura)#chamada a função
classificacao_imc = classificar_imc(imc)#chamada a função
sugestao = sugestao_atividade_fisica(classificacao_imc)#chamada a função

print(f"Seu IMC é: {imc:.2f}")#impressão das informações
print(f"Classificação: {classificacao_imc}")#impressão das informações
print(f"Sugestão de atividade física: {sugestao}")#impressão das informações