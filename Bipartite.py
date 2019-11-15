def is_bipartite(graph):
    """
    return True is graph is bipartite.

    attribute
    * graph is adjescent matrix
        * no self loop
        * no multi edge
        * graph[i][i]=0
    """
    N = len(graph)
    _N = len(graph[0])
    assert N == _N  # graph must be square matrix

    # unvisited=0
    # visited= 1 or-1
    visited = [0]*N
    visited[0] = 1
    Q = [0]
    while Q:
        cur = Q.pop()
        for next in range(N):
            if graph[cur][next] == 1:  # edge(cur,next) exsists
                if visited[next] == 0:
                    visited[next] = visited[cur]*(-1)
                    Q.append(next)
                elif visited[next] == visited[cur]:  # contradicted
                    return False
    return True
