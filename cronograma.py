from atividade import Atividade
from busca_binaria import buscaBinaria
import time


def cronograma(atividade):

    # Organiza pela data de termino
    atividade = sorted(atividade, key=lambda j: j.fim)

    tamanho = len(atividade)
    tabela_pontos = [0 for _ in range(tamanho)]
    tabela_pontos[0] = atividade[0].pontos

    for i in range(1, tamanho):
        add_ponto = atividade[i].pontos
        mais_recente = buscaBinaria(atividade, i)

        # Caso não existam conflitos com outras atividades
        if (mais_recente != -1):
            add_ponto += tabela_pontos[mais_recente]
            print(atividade[mais_recente].nome)

        tabela_pontos[i] = max(add_ponto, tabela_pontos[i - 1])

    return tabela_pontos[tamanho-1]


def main():

    atividades = []
    atividades.append(Atividade("Trabalho extra", "2 de Jan de 2018", "3 de Feb de 2018", 3))
    atividades.append(Atividade("Trabalho em grupo", "2 de Jan de 2018", "1 de Feb de 2018", 1))
    atividades.append(Atividade("Trabalho Final", "3 de Feb de 2018", "5 de Feb de 2018", 4))
    atividades.append(Atividade("Trabalho pratico", "5 de Feb de 2018", "6 de Jun de 2018", 2))
    atividades.append(Atividade("Trabalho em dupla", "6 de May de 2018", "1 de Jun de 2018", 4))

    print("\nO numero maximo de pontos atingidos com a organizacao das atividades eh:\n")
    inicio = time.time()
    print (cronograma(atividades))
    fim = time.time()

    print('\nTempo para organizacao do cronograma: ', fim - inicio, '\n')

if __name__ == '__main__':
    main()
