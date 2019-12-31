from api import *
import numpy as np
from igraph import Graph, plot

import numpy as np
import igraph


def get_network(users_ids, as_edgelist=True):
    vertices = ["It's me"]
    edges = []
    ids = []
    relat = {}
    for user_id in users_ids['response']['items']:
        name = user_id['first_name'] + user_id['last_name']
        user_id = user_id['id']
        ids.append(user_id)
        relat.update({user_id : len(relat.keys()) + 1})
        vertices.append(name)
    for user_id in users_ids['response']['items']:
        user_id = user_id['id']
        edges.append((0, relat[user_id]))
        friends = get_friends(user_id, 'sex')
        try:
            for friend in friends['response']['items']:
                lable = friend['id']
                if lable in ids:
                    edges.append((relat[user_id], relat[lable]))
        except:
            pass
    if as_edgelist:
        print(edges)
    else:
        n = max(max(i, j) for i, j in edges)
        matrix = np.zeros((n, n))
        for i, j in edges:
            matrix[i-1][j-1] = 1
        for row in matrix:
            print(row)
    g = Graph(vertex_attrs={"label":vertices},
            edges=edges, directed=False)
    N = len(vertices)
    visual_style = {}
    visual_style["layout"] = g.layout_fruchterman_reingold(
    maxiter=1500,
    area=N**2.5,
    repulserad=N**3)
    g.simplify(multiple=True, loops=True)
    plot_graph(g, visual_style)


def plot_graph(g, visual_style):
    communities = g.community_edge_betweenness(directed=False)
    clusters = communities.as_clustering()
    print(clusters)
    pal = igraph.drawing.colors.ClusterColoringPalette(len(clusters))
    g.vs['color'] = pal.get_many(clusters.membership)
    plot(g, **visual_style)


if __name__ == '__main__':
    get_network(get_friends(561313303, 'sex'), True)