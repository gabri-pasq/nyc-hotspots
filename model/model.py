import networkx as nx
from geopy.distance import geodesic
from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getPronviders(self):
        provaiders = DAO.getProvider()
        return provaiders

    def creaGrafo(self, provider, distanza):
        self.grafo = nx.Graph()
        locations = DAO.getLocation(provider)
        lista = []
        for l in locations:
            self.grafo.add_node(l)

        for n in  self.grafo.nodes:
            for m in self.grafo.nodes:
                d = geodesic((n.latitude, n.longitude),(m.latitude, m.longitude)).kilometers
                if n != m and d <= float(distanza):
                    self.grafo.add_edge(n,m, peso=distanza)
        for nodo in self.grafo.nodes:
            lista.append((nodo, len(list(self.grafo.neighbors(nodo)))))
        lista = sorted(lista, key=lambda x: x[1], reverse=True)
        return lista

    def grafoDetatails(self):
        return f"Numero di nodi: {self.grafo.number_of_nodes()}\nNumero di archi: {self.grafo.number_of_edges()}"