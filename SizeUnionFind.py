class UnionFind:
    """
    sizeによる実装
    """

    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1 for _ in range(N)]

    def find(self, x):
        """
        x: child
        ret-> node
        xのグループの代表を見つける
        """
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def union(self, x, y):
        """
        union (x ,y)
        x,y: node
        ret->None
        """
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]

    def same(self, x, y):
        """
        return true if x and y are in same group
        """
        return self.find(x) == self.find(y)

    def connectedNum(self, x):
        """
        return size of the group x belong to
        """
        return self.size[self.find(x)]

    def is_connected(self):
        """
        return true is all node is in one group
        """
        return self.connectedNum(0) == len(self.parent)

    def conpomentNum(self):
        """
        return num of component
        """
        par_set=set()
        for p in self.parent:
            par_set.add(self.find(p))
        return len(par_set)
