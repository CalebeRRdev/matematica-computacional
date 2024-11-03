def calcular_salario_final():
    # Solicitando informações do vendedor
    nome = input("\n\tDigite o nome do vendedor: ")
    ID = input("\n\tDigite o ID do vendedor: ")
    
    try:
        # Solicitando informações sobre o salário e comissões
        salario_fixo = float(input("\n\tDigite o salário fixo (em reais): "))
        comissao_por_carro = float(input("\n\tDigite a comissão por carro vendido (em reais): "))
        numero_de_carros = int(input("\n\tDigite o número de carros vendidos: "))
        total_vendas = float(input("\n\tDigite o total das vendas (em reais): "))
    except ValueError:
        print("\n\tErro: Certifique-se de inserir números válidos para salário, comissão, número de carros, e total de vendas.")
        return

    # Salário fixo inicial
    salario_final = salario_fixo

    # Lógica de cálculo
    if numero_de_carros > 0:
        salario_final += comissao_por_carro * numero_de_carros
        salario_final += 0.05 * total_vendas

        if numero_de_carros > 10:
            salario_final += 0.10 * total_vendas

    # Exibindo o resultado
    print("\n\t--- Detalhes do Vendedor ---")
    print(f"\n\tNome: {nome}")
    print(f"\n\tID: {ID}")
    print(f"\n\tSalário final: R$ {salario_final:.2f}")

# Chamando a função
calcular_salario_final()