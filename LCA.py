class LCA:
    """
    lowest common ancestor
    二分探索を用いる
    木において、頂点a,bの共通の祖先の中で、もっとも近いものを求める
    quertyの処理がO(log n) -> 二分探索、ダブリング
    """

    def __init__(self, V, adj, root=0):
        """
        root:木の根っこ
        V:頂点数
        adj:隣接行列
        """
        self.adj = adj
        # ceil(log2(V)) 最大で2の何乗の親まで辿るか
        #self.maxLog = int(((-log2(V))//1)*(-1))
        self.maxLog = 20
        # 各頂点の親
        self.parent = [[-1]*V for _ in range(self.maxLog+1)]
        # 各頂点の深さ
        self.depth = [0]*V
        # parent[0]とdepthの初期化
        self.__dfs(-1, root, 0)
        # parent[1:]の初期化
        for i in range(self.maxLog):
            for j in range(V):
                self.parent[i+1][j] = self.parent[i][self.parent[i][j]]

    def __dfs(self, par, cur, dep):
        """
        self.parentの初期化
        cur:現在のノード
        par:curの親
        dep:深さ
        """
        self.depth[cur] = dep
        self.parent[0][cur] = par
        for v in self.adj[cur]:
            if v == par:
                continue
            else:
                self.__dfs(cur, v, dep+1)

    def lca(self, a, b):
        """
        a,bのlcaを求める
        """
        if self.depth[a] > self.depth[b]:
            a, b = b, a

        # a,bを同じ深さまで持ってくる
        for i in range(self.maxLog):
            if (self.depth[b] - self.depth[a]) & 1 << i:
                b = self.parent[i][b]

        if a == b:
            return b

        for i in reversed(range(self.maxLog-1)):
            if self.parent[i][a] != self.parent[i][b]:
                a = self.parent[i][a]
                b = self.parent[i][b]
        return self.parent[0][a]

    def dist(self, a, b):
        """
        a,bの距離
        """
        lca = self.lca(a, b)
        return self.depth[a]+self.depth[b] - 2*self.depth[lca]
