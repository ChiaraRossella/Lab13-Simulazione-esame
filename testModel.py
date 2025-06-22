from model.model import Model

m=Model()
m.createGraph(1985)
print(f"Grafo correttamente creato:")
print(f"Numero di nodi: {m.get_num_nodes()}")
print(f"Numero di archi: {m.get_num_archi()}")
pilota, score= m.getBestPilota()
print(f"Best Driver: {pilota}, with score {score}")
solB, score = m.getDreamTeam(2)
print(f"best team {solB}")
print(f"score {score}")
