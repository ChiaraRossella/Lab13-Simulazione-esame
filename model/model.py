import copy

import networkx as nx

from database.DAO import DAO
from model.pilota import Pilota


class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self._nodes = None
        self._archi = None
        self._solBest = None
        self._score = 10000

    def getDreamTeam(self, k: int):
        self._solBest = None
        self._score = 10000
        parziale = []
        rimanenti = list(self._grafo.nodes)
        for n in self._grafo:
            parziale.append(n)
            rimanenti.remove(n)
            self._ricorsione(parziale, k, rimanenti)
            parziale.remove(n)
            rimanenti.append(n)
        return self._solBest, self._score

    def _ricorsione(self, parziale: list, k: int, rimanenti: list):
        score = self.getScoreTeam(parziale)
        if len(parziale)==k:
            if score < self._score:
                self._score = score
                self._solBest = copy.deepcopy(parziale)
            return

        for n in rimanenti:
            rimanenti.remove(n)
            parziale.append(n)
            self._ricorsione(parziale, k, rimanenti)
            rimanenti.append(n)
            parziale.remove(n)

    def getScoreTeam(self, team: list):
        score = 0
        for n in team:
            eIn = self._grafo.in_edges(n, data=True)
            for arco in eIn:
                if arco[0] not in team:
                    score += arco[2]['weight']
        return score

    def get_years(self):
        return DAO.get_all_years()

    def get_nodes(self, anno: int):
        return DAO.get_all_nodes(anno)

    def get_archi(self, anno: int):
        return DAO.get_all_archi(anno)

    def createGraph(self, anno: int):
        self._grafo.clear()
        self._nodes = self.get_nodes(anno)
        self._grafo.add_nodes_from(self._nodes)
        for n1 in self._grafo:
            for n2 in self._grafo:
                if n1 != n2:
                    peso = DAO.getVittorie(anno, n1.driverId, n2.driverId)
                    if peso > 0:
                        self._grafo.add_edge(n1, n2, weight=peso)

    def get_num_archi(self):
        return self._grafo.number_of_edges()

    def get_num_nodes(self):
        return self._grafo.number_of_nodes()

    def getBestPilota(self):
        best = 0
        bestPilota = None
        for n in self._grafo:
            grado = self.getScore(n)
            if (grado) > best:
                bestPilota = n
                best = grado
        return bestPilota, best

    def getScore(self, n: Pilota):
        out = self._grafo.out_edges(n, data=True)
        gOut = sum([c[2]['weight'] for c in out])
        edgesin = self._grafo.in_edges(n, data=True)
        gIn = sum([c[2]['weight'] for c in edgesin])
        return gOut - gIn
