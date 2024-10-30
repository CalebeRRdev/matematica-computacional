def avalia_condicoes(P, Q, M):
    """
    Avalia o valor de R com base nas condições descritas.
    
    Args:
    P (bool): Ana vai à festa.
    Q (bool): Bruno vai à festa.
    M (bool): Bruno traz música.
    
    Returns:
    bool: Valor de R (a festa é animada) para as condições dadas.
    """
    # Avalia cada condição lógica
    cond1 = (not P) or Q                 # P -> Q
    cond2 = (not (P or Q)) or R          # (P ∨ Q) -> R
    cond3 = (not P) or (not M or R)      # ¬P -> (M -> R)

    # R é verdadeiro se todas as condições são satisfeitas
    R = cond1 and cond2 and cond3
    return R

def tabela_verdade():
    """
    Constrói e exibe a tabela verdade para as proposições P, Q, M e avalia R para cada caso.
    """
    print(f"{'P':<5} {'Q':<5} {'M':<5} {'R':<5}")
    print("=" * 20)
    for P in [True, False]:
        for Q in [True, False]:
            for M in [True, False]:
                R = avalia_condicoes(P, Q, M)
                print(f"{P:<5} {Q:<5} {M:<5} {R:<5}")

# Executa a função para exibir a tabela verdade completa
tabela_verdade()
