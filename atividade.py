import time
from datetime import datetime


class Atividade(object):

    def __init__(self, nome, inicio, fim, pontos):
        self.nome = nome
        # d = dia, b = mes, y = ano, H = horas
        self.inicio = int(time.mktime(datetime.strptime(
                                    inicio, "%d de %b de %Y").timetuple()))
        self.fim = int(time.mktime(datetime.strptime(
                                    fim, "%d de %b de %Y").timetuple()))
        self.pontos = pontos

    def __repr__(self):
        return str((self.nome, self.inicio, self.fim, self.pontos))
