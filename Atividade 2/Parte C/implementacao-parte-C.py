def verifica_interseccao_bissetriz_externa(lado_oposto, lado1, lado2):
    """
    Verifica se a bissetriz externa intercepta o prolongamento do lado oposto.
    
    Args:
    lado_oposto (float): comprimento do lado oposto à bissetriz externa.
    lado1 (float): comprimento de um dos lados adjacentes ao ângulo.
    lado2 (float): comprimento do outro lado adjacente ao ângulo.
    
    Returns:
    str: mensagem indicando se a intersecção ocorre ou não.
    """
    # Verifica se os lados adjacentes são iguais
    if lado1 == lado2:
        return "A bissetriz externa NÃO intercepta o prolongamento do lado oposto, pois os lados adjacentes são iguais."
    else:
        return "A bissetriz externa INTERCEPTA o prolongamento do lado oposto, pois os lados adjacentes são diferentes."

# Exemplo de uso:
lado_oposto = float(input("Digite o comprimento do lado oposto à bissetriz externa: "))
lado1 = float(input("Digite o comprimento de um lado adjacente: "))
lado2 = float(input("Digite o comprimento do outro lado adjacente: "))

# Chama a função e exibe o resultado
resultado = verifica_interseccao_bissetriz_externa(lado_oposto, lado1, lado2)
print("\n", resultado)
