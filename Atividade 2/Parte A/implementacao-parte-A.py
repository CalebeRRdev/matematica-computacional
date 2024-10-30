def bissetriz_interna(lado_oposto, lado1, lado2):
    """
    Calcula a razão entre as partes divididas pela bissetriz interna do ângulo.
    
    Args:
    lado_oposto (float): comprimento do lado oposto ao ângulo da bissetriz.
    lado1 (float): comprimento de um dos lados adjacentes.
    lado2 (float): comprimento do outro lado adjacente.
    
    Returns:
    tuple: razão (lado1/lado2) e os comprimentos dos segmentos divididos ou uma mensagem de erro
    """
    # Verifica se a soma dos lados adjacentes é zero
    if lado1 + lado2 == 0:
        return None, "Erro: A soma dos lados adjacentes não pode ser zero."
    
    razao = lado1 / lado2
    x = (lado_oposto * lado1) / (lado1 + lado2)
    y = lado_oposto - x
    return razao, x, y

# Exemplo de uso:
lado_oposto = float(input("\n\tDigite o comprimento do lado oposto à bissetriz: "))
lado1 = float(input("\n\tDigite o comprimento de um lado adjacente: "))
lado2 = float(input("\n\tDigite o comprimento do outro lado adjacente: "))

resultado = bissetriz_interna(lado_oposto, lado1, lado2)
if resultado[0] is None:
    print(resultado[1])
else:
    razao, x, y = resultado
    print(f"\n\tA razão entre os segmentos é {razao:.2f}.")
    print(f"\n\tOs segmentos são {x:.2f} e {y:.2f}.")
