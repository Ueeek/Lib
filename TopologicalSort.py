def topological_sort(V, E_in, E_from):
    '''
    #Note
    -----------------
    Order: O(|V|+|E|)

    # parameters
    ------------------
    V:N(node)
    E_from: [ [ pointing nodes]]]
    E_in:[[pointed nodes]]

    # return
    ret: list of node(topologycal sorted)
    '''

    # count num of pointed nodes for each nodes
    ret = []

    cnt = [0]*V  # cnt[i] is num of pointed nodes
    Q = []
    for v in range(V):
        cnt[v] = len(E_in[v])
        if cnt[v] == 0:
            "cnt[v]=0 -> node v　is root(start of algorithm)"
            Q.append(v)

    while Q:
        del_node = Q.pop()
        ret.append(del_node)
        for j in E_from[del_node]:
            "delete edge from del_node to other node"
            cnt[j] -= 1
            if cnt[j] == 0:
                Q.append(j)

    return ret
