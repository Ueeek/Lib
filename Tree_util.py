"""
* adjの入力は以下を前提とする
    N = int(input())
    edges = [(map(lambda x: int(x) - 1, input().split())) for _ in range(N - 1)]
    adj = [set() for _ in range(N)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
* adjを引数に持ってるやつは、globalにadjを持っておけば必要ないせつ
"""

from typing import *

def get_child(adj:List[List[int]],root:int)-> List[List[int]]:
    """
    RETURN:
        child[i] = list of index of child nodes of i
    """

    N = len(adj)
    visited = set()
    parent=[-1]*N
    child = [[] for _ in range(N)]

    visited.add(root)
    Q = [root]

    while Q:
        cur = Q.pop()
        for nex in adj[cur]:
            if nex in visited:
                continue
            else:
                Q.append(nex)
                child[cur].append(nex)
                visited.add(nex)
    return child

def get_parent(adj:List[List[int]],root:int)-> List[int]:
    """
    RETURN:
        parent[i]: parent node idx of node i
    """

    child = get_child(adj,root)
    N = len(adj)

    parent = [-1]*N
    for par in range(N):
        for chi in child[par]:
            parent[chi] = par
            
    return parent


def post_order_traversal_gelnerator(adj:List[List[int]],root:int):
    """
    再帰なしで post_order_traversal

    Return:
        post_order_traversal の順番にreturn
    """


    child = get_child(adj,root)

    Q = [root]
    visited = set()

    while Q:
        cur = Q.pop()

        if cur in visited:
            continue

        if len(child[cur])==0:
            #leaf
            yield cur
            visited.add(cur)

        elif all(chi in visited for chi in child[cur]):
            #all child is visited
            yield cur
            visited.add(cur)

        else:
            Q.append(cur)
            for chi in child[cur]:
                if chi in visited:
                    continue
                Q.append(chi)

def tree_dfs_generator(adj, root):
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
    depth = [-1] * N

    # calc depth
    Q = [root]
    depth[root] = 0
    while Q:
        P = []
        for cur in Q:
            for nex in adj[cur]:
                if depth[nex] == -1:
                    depth[nex] = depth[cur] + 1
                    P.append(nex)
        Q = P

    # tree must be connected
    assert all(d >= 0 for d in depth), " ".join(map(str, depth))
    depth_K = list(sorted([[depth[i], i] for i in range(N)], reverse=True))
    for dep, idx in depth_K:
        yield (dep, idx)


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

    # 適当な頂点からdfs
    depth1 = [None] * N
    root1 = 0
    depth1[root1] = 0
    used1 = {root1}
    Q1 = [root1]

    while Q1:
        cur = Q1.pop()
        for nex in adj[cur]:
            if nex in used1:
                continue
            depth1[nex] = depth1[cur] + 1
            Q1.append(nex)
            used1.add(nex)

    root2 = depth1.index(max(depth1))
    depth2 = [None] * N
    depth2[root2] = 0
    used2 = {root2}
    Q2 = [root2]

    while Q2:
        cur = Q2.pop()
        for nex in adj[cur]:
            if nex in used2:
                continue
            depth2[nex] = depth2[cur] + 1
            Q2.append(nex)
            used2.add(nex)

    return max(depth2)


def calc_dist_from_root(root: int, adj: List[List]) -> List[int]:
    """
    rootを根とした気で、rootからの距離を求める

    Args:
        root: 木の根のid
        adj: 隣接リスト
    Return:
        dist_from_root:List[int] i-th nodeまでの距離
    """
    dist_from_root = [0] * len(adj)
    visited = {root}
    Q = [root]
    while Q:
        cur = Q.pop()
        for a in adj[cur]:
            if a in visited:
                continue
            else:
                visited.add(a)
                Q.append(a)
                dist_from_root[a] = dist_from_root[cur] + 1

    return dist_from_root


def calc_num_child(root: int, adj: List[List]) -> List[int]:
    """
    rootを根とした有向木で、subtreeのノード数を求める。
    自分は含まれない
    Args:
        root: 木の根のid
        adj: 隣接リスト
    Return:
        num_child:List i-thノードのこの数
    """

    num_child = [0] * len(adj)
    visited = set()
    for (_, idx) in tree_dfs_generator(adj, root):
        visited.add(idx)
        for a in adj[idx]:
            if a in visited:
                continue
            else:
                num_child[a] += num_child[idx] + 1

    return num_child
