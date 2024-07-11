import random

#Função que joga os dados
def rolar_d6():
    dado1 = (random.randint(1, 6))
    return dado1

#inverte a string
def inverter_string(s):
    return s[::-1]


# Número de jogadas desejado
numero_jogadas =  2

# Lista para armazenar os resultados
resultados = []

# Jogadas
for num in range(numero_jogadas):
    resultado_dado1 = rolar_d6()
    resultados.append(resultado_dado1)

# Exibindo os resultados
for i, (dado1) in enumerate(resultados, 1):
    print(f"Jogada {i}: Dado: {dado1}")

# Tabela de nomes
tabela = {
    1: ["Plaft", "Plin", "Tik", "Tok", "Bash", "Cricri"],
    2: ["Glub", "Tim", "Ranço", "Yhaa", "Vrum", "Aiaiai"],
    3: ["Crash", "Zzzz", "Sussa", "Bibi", "Boom", "Bum"],
    4: ["Spray", "Cringe", "Sopa", "Ovo", "Ban", "Nhack"],
    5: ["Bing", "Riso", "Slash", "Coff", "Ugh", "Sniff"],
    6: ["Última coisa que comeu","Última coisa que comeu",
        "Última coisa que comeu", "Inverta seu nome", "Inverta seu nome",
        "Inverta seu nome"] 
}

# Escolhendo o nome correspondente
if resultados[0] in [4, 5, 6] and resultados[1] == 6:
    nome_cadastro = input("Digite seu nome: ")
    nome_escolhido = inverter_string(nome_cadastro)
else:
    nome_escolhido = tabela[resultados[1]][resultados[0] - 1]

#print(f" Nome escolhido: {nome_escolhido}")

def nome():
    nome = str(nome_escolhido)
    return nome