def buscaBinaria(atividade, index_atividade):

    inicio = 0
    fim = index_atividade - 1

    while inicio <= fim:
        meio = ((inicio + fim) // 2)
        if atividade[meio].fim <= atividade[index_atividade].inicio:
            if atividade[meio + 1].fim <= atividade[index_atividade].inicio:
                inicio = meio + 1
            else:
                return meio
        else:
            fim = meio - 1
    return -1
