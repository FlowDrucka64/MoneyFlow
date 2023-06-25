import networkx as nx
import json
import csv
from pprint import *

NO_CON = "NAN"

with open('data/neighbours.json', 'r') as file:
    data = json.load(file)


countries = {}
for node in data["nodes"]:
    countries[node["name"]] = set()

for link in data["links"]:
    if link["source"] in countries:
        countries[link["source"]].add(link["target"])
    if link["source"] in countries:
        countries[link["target"]].add(link["source"])

for country in countries:
    countries[country] = list(countries[country])


graph = nx.Graph()

graph.add_nodes_from(countries.keys())

for country,neighbours in countries.items():
    for neighbour in neighbours:
        graph.add_edge(country,neighbour)

with open('data/neighbour_distance_matrix.csv', 'w', newline="\n") as file:
    writer = csv.writer(file)
    line = ["FROM/TO"]
    for country in countries:
        line.append(country)
    writer.writerow(line)

    for _source in countries:
        line = [_source]
        for _target in countries:
            try:
                shortest_path = nx.shortest_path(graph,source=_source, target=_target)
                line.append(len(shortest_path))
            except:
                line.append(NO_CON)
        writer.writerow(line)
