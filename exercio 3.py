
def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial):#calcula a glicemia do paciete em jejum e pós-prandial


    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200:#estabelece uma estrutura condicional
        return "Diabetes"#se glicemia_em_jejum for maior ou igual a 126, ou glicemia_pos_prandial maior ou igual a 200, é retornado como diabetes
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:
        return "Pré-diabetes"#se glicemia_em_jejum for menor do que 126, ou glicemia_pos_prandial menor ou igual a 200, é retornado como normal
    else:
        return "Normal"

glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): "))#lê o valor da glicemia em jejum
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))#lê o valor da glicemia pós-pandrial

resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)#é chamada a função para diagnosticar o diabetes
print(f"O diagnóstico é: {resultado}")# é impresso o resultado, ou seja, se está, ou não, com os níveis normais de insulina.
