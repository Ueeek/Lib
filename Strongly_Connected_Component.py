import sys
sys.setrecursionlimit(10**9)
def strongly_connected_componen(adj):
    """
    強連結成分を求める

    :param: adj　adjacent list
    """
    N = len(adj)
    adj_rev=[[] for _ in range(N)]


    for i in range(N):
        for j in adj[i]:
            adj_rev[j].append(i)

    group=[None]*N
    used=[False]*N
    order=[]

    # dfsをして、帰りがけ順番を記録
    def dfs(s):
        used[s]=True
        for t in adj[s]:
            if not used[t]:
                dfs(t)
        order.append(s)

    def rdfs(s,col):
        group[s]=col
        used[s]=True
        for t in adj_rev[s]:
            if not used[t]:
                rdfs(t,col)

    for i in range(N):
        if not used[i]:
            dfs(i)

    used = [False]*N
    label= 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s,label)
            label += 1

    groups=[[] for _ in range(label)]
    for i,g in enumerate(group):
        groups[g].append(i)
    # sccのgroupごとに属するidxのlist
    return groups


def strongly_connected_component_non_rec(adj,adj_rev):
    """
    強連結成分を求める

    ### (注意) adjに、破壊的操作をするよ!

    :param: adj　adjacent list
    :return: list[list] ret[i]=> list of idx s.t. belong to scc group i
    """
    N = len(adj)

    # dfs
    visited=[False]*N
    # dfsの帰りがけ順序
    order=[]
    for s in range(N):
        if visited[s]:
            continue

        #dfs from s
        stack=[s]
        visited[s]=True
        while stack:
            node = stack.pop()
            while adj[node]: #for文でやると、毎回 for nex in adj[cur]のloopが辛いので、visitedしたら、adjから消していく
                nex = adj[node].pop()
                if visited[nex]:
                    continue

                stack.append(node)
                stack.append(nex)
                visited[nex]=True
                break
            else: #leat or all adj node is visited
                order.append(node)
    
    # rev_dfs
    label = 0
    group=[None]*N
    for s in reversed(order):
        if group[s] is not None:
            continue

        stack=[s]
        group[s]=label
        while stack:
            node = stack.pop()
            for nex in adj_rev[node]:
                if group[nex] is not None:
                    continue
                group[nex]=label
                stack.append(nex)
        label+=1


    groups=[[] for _ in range(label)]
    for i,g in enumerate(group):
        groups[g].append(i)
    # sccのgroupごとに属するidxのlist
    return groups
