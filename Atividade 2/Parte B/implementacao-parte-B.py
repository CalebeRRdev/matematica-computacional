def bissetriz_externa(lado_oposto, lado1, lado2):
    """
    Calcula a divisão do lado oposto pela bissetriz externa.
    
    Args:
    lado_oposto (float): comprimento do lado oposto à bissetriz externa.
    lado1 (float): comprimento de um dos lados adjacentes ao ângulo.
    lado2 (float): comprimento do outro lado adjacente ao ângulo.
    
    Returns:
    tuple: razão (lado1 / lado2) e os comprimentos dos segmentos formados pela bissetriz externa.
    """
    # Verifica se os lados adjacentes são iguais para evitar divisão por zero
    if lado1 == lado2:
        return None, "Divisão por zero: os lados adjacentes não podem ser iguais."

    # Calcula a razão entre os lados adjacentes ao ângulo
    razao = lado1 / lado2

    # Calcula os segmentos formados pela bissetriz externa
    x = (lado_oposto * lado1) / (lado1 - lado2)
    y = x - lado_oposto

    return razao, x, y

# Exemplo de uso:
lado_oposto = float(input("\n\tDigite o comprimento do lado oposto à bissetriz externa: "))
lado1 = float(input("\n\tDigite o comprimento de um lado adjacente: "))
lado2 = float(input("\n\tDigite o comprimento do outro lado adjacente: "))

# Chama a função e exibe os resultados
resultado = bissetriz_externa(lado_oposto, lado1, lado2)
if resultado[0] is None:
    print(f"\n\tErro: {resultado[1]}")
else:
    razao, x, y = resultado
    print(f"\n\tA razão entre os segmentos é {razao:.2f}.")
    print(f"\n\tOs segmentos formados pela bissetriz externa são {x:.2f} e {y:.2f}.")
