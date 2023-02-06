INF = 9999999


def prim(N, G, selected_node, no_edge):
    # printing for edge and weight
    print("Edge : Weight\n")
    while (no_edge < N - 1):
        minimum = INF
        a = 0
        b = 0
        for m in range(N):
            if selected_node[m]:
                for n in range(N):
                    if ((not selected_node[n]) and G[m][n]) and minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
        print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
        selected_node[b] = True
        no_edge += 1
    return

if __name__ == "__main__":

    """
     Goal: To find Min Span Tree
     Steps: For each connected node, choose the minimum edge for next connection, always.
     Reason: ???
    """

    # number of vertices in graph
    N = 5
    # creating graph by adjacency matrix method
    G = [[0, 19, 5, 0, 0],
         [19, 0, 5, 9, 2],
         [5, 5, 0, 1, 6],
         [0, 9, 1, 0, 1],
         [0, 2, 6, 1, 0]]

    selected_node = [0, 0, 0, 0, 0]
    no_edge = 0 # Number of Node without edge
    selected_node[0] = True

    prim(N, G, selected_node, no_edge)
