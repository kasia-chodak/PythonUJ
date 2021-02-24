import json
with open('przystanki.json', "r", encoding='utf-8') as read_file:
    data_tram_stops = json.load(read_file)['przystanki']
with open('tramwaje.json', "r", encoding='utf-8') as read_file:
    data_trams = json.load(read_file)

index_list = {data_tram_stops[index]: index for index in range(len(data_tram_stops))}


def get_stop_key(stop_name):
    return index_list[stop_name]


# generowanie grafu
vertices = [[ 2000 for _ in range(len(data_tram_stops))] for _ in range(len(data_tram_stops))]


def generate_graph():
    for tram in data_trams['tramwaje']:
        for stop_ndx in range(0, len(tram['tprzystanki'])):
            for neighbour_stop_ndx in range(0, len(tram['tprzystanki'])):
                distance = abs(stop_ndx - neighbour_stop_ndx)
                current_ndx = tram['tprzystanki'][stop_ndx]['name']
                neighbour_ndx = tram['tprzystanki'][neighbour_stop_ndx]['name']
                if vertices[get_stop_key(current_ndx)][get_stop_key(neighbour_ndx)] > distance:
                    vertices[get_stop_key(current_ndx)][get_stop_key(neighbour_ndx)] = distance


generate_graph()

edge_graph = []
edges = 0
for v in range(len(vertices)):
    for w in range(len(vertices[v])):
        if vertices[v][w] != 2000 and vertices[v][w] != 0:
            edges += 1
            if (w, v, vertices[v][w]) not in edge_graph:
                edge_graph.append((v, w, vertices[v][w]))
edges //= 2
max_size = 20000


def find_min_distance(distance_list, visited):
    min_dist = max_size
    min_dist_ndx = -1
    for v in range(len(distance_list)):
        if not visited[v] and distance_list[v] < min_dist:
            min_dist = distance_list[v]
            min_dist_ndx = v
    return min_dist_ndx


def dijkstra(przystanek_start, przystanek_stop):
    big_number = max_size
    shortest_dist = [big_number] * len(data_tram_stops)
    index_start = get_stop_key(przystanek_start)
    index_stop = get_stop_key(przystanek_stop)
    shortest_dist[index_start] = 0
    visited_nodes = [False] * len(data_tram_stops)
    for node in range(len(data_tram_stops)):
        shortest_dist[node] = big_number
    shortest_dist[index_start] = 0

    for wierzcholek in range(len(data_tram_stops)):
        a = find_min_distance(shortest_dist, visited_nodes)
        visited_nodes[a] = True
        for v in range(len(data_tram_stops)):
            if vertices[a][v] != 2000 and vertices[a][v] > 0 and not visited_nodes[v] and shortest_dist[v] > shortest_dist[a] + vertices[a][v]:
                shortest_dist[v] = shortest_dist[a] + vertices[a][v]
    return shortest_dist[index_stop]


print(dijkstra('Bieńczycka', 'Czerwone Maki P+R'))


def bellman_ford(przystanek_start, przystanek_stop):
    index_start = get_stop_key(przystanek_start)
    index_stop = get_stop_key(przystanek_stop)
    distance = [max_size] * len(data_tram_stops)
    distance[index_start] = 0
    for i in range(len(data_tram_stops) - 1):
        for j in range(edges):
            if distance[edge_graph[j][0]] + edge_graph[j][2] < distance[edge_graph[j][1]]:
                distance[edge_graph[j][1]] = distance[edge_graph[j][0]] + edge_graph[j][2]

    # Ten fragment jeżeli wagi są ujemne
    for i in range(edges):
        u = edge_graph[i][0]
        v = edge_graph[i][1]
        weight = edge_graph[i][2]
        if distance[u] != max_size and distance[u] + weight < distance[v]:
            print('Graf zawiera cykl o negatywnych wagach')
    return distance[index_stop]


print(bellman_ford('Bieńczycka', 'Czerwone Maki P+R'))


def floyd_warshall(przystanek_start, przystanek_stop):
    distance = [x.copy() for x in vertices]
    index_start = get_stop_key(przystanek_start)
    index_stop = get_stop_key(przystanek_stop)
    for k in range(len(data_tram_stops)):
        for v in range(len(data_tram_stops)):
            for u in range(len(data_tram_stops)):
                distance[v][u] = min(distance[v][u], distance[v][k] + distance[k][u])
    return distance[index_start][index_stop]


# Bardzo bardzo wolne
# print(floyd_warshall('Bieńczycka', 'Czerwone Maki P+R'))
