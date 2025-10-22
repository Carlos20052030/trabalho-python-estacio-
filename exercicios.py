import random
import datetime

# 1. Função que recebe um número inteiro e devolve o seu dobro
def numero_dobro(numero):
    return numero * 2

# 2. Função que imprime os 10 primeiros termos de uma PA
def progressao_aritmetica(primeiro, razao):
    print("Progressão Aritmética:")
    for i in range(10):
        termo = primeiro + i * razao
        print(termo, end=' ')
    print("\n")

# 3. Função que imprime os 10 primeiros termos de uma PG
def progressao_geometrica(primeiro, razao):
    print("Progressão Geométrica:")
    for i in range(10):
        termo = primeiro * (razao ** i)
        print(termo, end=' ')
    print("\n")

# 4. Função que retorna um anagrama de uma palavra
def gerar_anagrama(palavra):
    letras = list(palavra)
    random.shuffle(letras)
    return ''.join(letras)

# 5. Função que exibe a data por extenso
def data_por_extenso(dia, mes, ano):
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    if 1 <= mes <= 12:
        print(f"{dia} de {meses[mes - 1]} de {ano}")
    else:
        print("Mês inválido!")

# Testes das funções
if __name__ == "__main__":
    print("1. Dobro de 7:", numero_dobro(7))
    print("\n2. PA com primeiro termo 1 e razão 2:")
    progressao_aritmetica(1, 2)
    print("3. PG com primeiro termo 2 e razão 3:")
    progressao_geometrica(2, 3)
    print("4. Anagrama de 'amor':", gerar_anagrama("amor"))
    print("5. Data por extenso (01/01/2000):")
    data_por_extenso(1, 1, 2000)