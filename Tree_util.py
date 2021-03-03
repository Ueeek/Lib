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

