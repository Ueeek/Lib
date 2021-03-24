def tree_dfs_generator(adj,root):
    """
    tree_dfsを、深いノードから辿ることで、再帰無しでやる
    
    Arguents:
        root: root node id of tree
        adj: tree(bi-dirでも、dirでもいけるはず)

    Return:
        rootから遠いノードから、(dep,node_idx)をreturnしていく
        next_node: yield:(depth,idx)
    """


    N = len(adj)
    depth=[-1]*N

    #calc depth
    Q=[root]
    depth[root]=0
    while Q:
        P=[]
        for cur in Q:
            for nex in adj[cur]:
                if depth[nex] ==-1:
                    depth[nex]=depth[cur]+1
                    P.append(nex)
        Q=P

    #tree must be connected
    assert all(d>=0 for d in depth)," ".join(map(str,depth))
    depth_K = list(sorted([[depth[i],i] for i in range(N)],reverse=True))
    for dep,idx in depth_K:
        yield (dep,idx)

def tree_diameter(adj):
    """
    木の直径を求める
    *適当なところから一番遠い頂点を求める。
    * そいつから一番遠い頂点までの距離が直径

    Arguments:
        adj: 木を構成する隣接リスト
    Return:
        diamter: 木の直径(int)
    """

    N = len(adj)

    #適当な頂点からdfs
    depth1=[None]*N
    root1=0
    depth1[root1]=0
    used1={root1}
    Q1=[root1]

    while Q1:
        cur = Q1.pop()
        for nex in adj[cur]:
            if nex in used1:
                continue
            depth1[nex]=depth1[cur]+1
            Q1.append(nex)
            used1.add(nex)

    root2 = depth1.index(max(depth1))
    depth2=[None]*N
    depth2[root2]=0
    used2={root2}
    Q2=[root2]

    while Q2:
        cur = Q2.pop()
        for nex in adj[cur]:
            if nex in used2:
                continue
            depth2[nex]=depth2[cur]+1
            Q2.append(nex)
            used2.add(nex)

    return max(depth2)
