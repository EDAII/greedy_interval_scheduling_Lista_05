from atividade import Atividade
from busca_binaria import buscaBinaria


def cronograma(atividade):

    # Organiza pela data de fim
    atividade = sorted(atividade, key=lambda j: j.fim)
    tamanho = len(atividade)

    tabela_pontos = [0 for _ in range(tamanho)]

    tabela_pontos[0] = atividade[0].pontos

    for i in range(1, tamanho):
        add_ponto = atividade[i].pontos
        mais_recente = buscaBinaria(atividade, i)
        if (mais_recente != -1):
            add_ponto += tabela_pontos[mais_recente]

        tabela_pontos[i] = max(add_ponto, tabela_pontos[i - 1])

    return tabela_pontos[tamanho-1]


# atividades = [Atividade(), Atividade()]
