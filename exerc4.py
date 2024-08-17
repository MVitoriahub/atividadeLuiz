def calcular_media_e_aprovacao(notas, nota_minima_aprovacao):
    total_notas = 0#considera como nulo o valor atual do total de notas
    num_alunos = len(notas)#conta o número de notas
    aprovados = []#é uma lista vazia que armazenará os aprovados
    reprovados = []#é uma lista vazia que armazenará os reprovados

    for aluno, nota in notas.items():#estabelece uma estrutura condicional
        total_notas += nota#adiciona a nota ao total das notas dos alunos
        if nota >= nota_minima_aprovacao:# se a nota mínima for atingida, soma-se a lista de alunos aprovado
            aprovados.append(aluno)
        else:
            reprovados.append(aluno)#se a nota mínima não for atingida, soma-se a lista de alunos reprovados

    media_turma = total_notas / num_alunos#calcula a média da turma

    return media_turma, aprovados, reprovados#retorna media da turma, os reprovados e aprovados

notas = {#informa o nome dos alunos e suas notas
    "Alice": 85,
    "Bruno": 72,
    "Carlos": 60,
    "Diana": 95,
    "Eduardo": 55
}

nota_minima_aprovacao = 70#informa a nota minima para a aprovação

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)#chama a função para cálculo da média , dos reprovados e dos aprovados

print(f"Média da turma: {media_turma:.2f}")#printa a média da turma
print(f"Alunos aprovados: {', '.join(aprovados)}")#printa os aprovados
print(f"Alunos reprovados: {', '.join(reprovados)}")#printa os reprovados
