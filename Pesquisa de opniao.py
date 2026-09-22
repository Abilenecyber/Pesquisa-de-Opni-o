# =================================================================
# ATIVIDADE: PESQUISA DE OPNIÃO - TudoWeb
# # =================================================================

excelente = 0
ruim = 0

print("--- INICIANDO PESQUISA ---")

# Repete 50 vezes para o teste inicial 
for i in range(1, 51):
    print("-----------------------------------")
    print("Entrevistado numero:", i)
    
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    print("Opniao sobre o atendimento:")
    print("1: EXCELENTE | 2: BOM | 3: RUIM")
    opiniao = int(input("Digite o numero da opcao: "))
    
    # Verifica a resposta usando estruturas de decisão simples
    if opiniao == 1:
        excelente = excelente + 1
    
    if opiniao == 3:
        ruim = ruim + 1

# Exibição dos resultados finais
print("\n========================================")
print("RESULTADO DA PESQUISA")
print("========================================")
print("a) Quantidade de respostas 'EXCELENTE':", excelente)
print("b) Quantidade de respostas 'RUIM':", ruim)
print("Total de clientes entrevistados: 10")
print("========================================")
