# Função para verificar semelhança pelo critério LAL
def verifica_lal(tri1, tri2):
    lados1_proporcionais = (tri1["lado1"] / tri2["lado1"] == tri1["lado2"] / tri2["lado2"])
    angulos_iguais = (tri1["angulo_entre"] == tri2["angulo_entre"])
    return lados1_proporcionais and angulos_iguais

# Função para verificar semelhança pelo critério AA
def verifica_aa(tri1, tri2):
    angulo1_igual = (tri1["angulo1"] == tri2["angulo1"])
    angulo2_igual = (tri1["angulo2"] == tri2["angulo2"])
    return angulo1_igual and angulo2_igual

# Função para verificar semelhança pelo critério LLL
def verifica_lll(tri1, tri2):
    lado1_proporcional = (tri1["lado1"] / tri2["lado1"] == tri1["lado2"] / tri2["lado2"])
    lado2_proporcional = (tri1["lado2"] / tri2["lado2"] == tri1["lado3"] / tri2["lado3"])
    return lado1_proporcional and lado2_proporcional

# Função principal para determinar a semelhança dos triângulos
def verifica_semelhanca(tri1, tri2):
    if verifica_lal(tri1, tri2):
        return "\n\tOs triângulos são semelhantes pelo critério LAL.\n"
    elif verifica_aa(tri1, tri2):
        return "\n\tOs triângulos são semelhantes pelo critério AA.\n"
    elif verifica_lll(tri1, tri2):
        return "\n\tOs triângulos são semelhantes pelo critério LLL.\n"
    else:
        return "\n\tOs triângulos não são semelhantes."

# Função para capturar as informações de um triângulo
def obter_dados_triangulo(numero):
    print(f"\n\tDigite os valores para o Triângulo {numero}:")
    lado1 = float(input("\n\tLado 1: "))
    lado2 = float(input("\n\tLado 2: "))
    lado3 = float(input("\n\tLado 3: "))
    angulo1 = float(input("\n\tÂngulo 1: "))
    angulo2 = float(input("\n\tÂngulo 2: "))
    angulo_entre = float(input("\n\tÂngulo entre Lado 1 e Lado 2: "))
    return {
        "lado1": lado1,
        "lado2": lado2,
        "lado3": lado3,
        "angulo1": angulo1,
        "angulo2": angulo2,
        "angulo_entre": angulo_entre
    }

# Capturando os dados dos triângulos
triangulo1 = obter_dados_triangulo(1)
triangulo2 = obter_dados_triangulo(2)

# Teste de semelhança
resultado = verifica_semelhanca(triangulo1, triangulo2)
print(resultado)
