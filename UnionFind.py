class UnionFind:
    def __init__(self, size):
        """
        size:頂点の数
        parent[x]->parent of x
        rank[x] -> height of tree of x
        conN[x] ->size of group x belong
        """
        self.parent = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]
        self.conN = [1 for _ in range(size)]

    def find(self, x):
        """
        xのrootを返す
        """
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def union(self, x, y):
        """
        x,yを同じグループとしてまとめる
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.big[y] += self.big[x]
        else:
            self.parent[y] = x
            self.big[x] += self.big[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        """
        xとyが同じグループならTrue
        """
        return self.find(x) == self.find(y)

    def component(self):
        """
        各連結成分のrootの集合を返す
        len()をとれば連結成分の数が求められる
        return-> set()
        """
        comp = set()
        for i in self.parent:
            p = self.find(i)
            comp.add(p)
        return comp

    def connectedNum(self, x):
        """
        xが属している集合の要素のサイズを返す
        """
        p = self.find(x)
        return self.conN(p)

    def __str__(self):
        """
        for debug
        クラスのlistの情報を出力
        """
        ret = "parents\n"
        ret += " ".join(map(str, self.parent))
        ret += '\n'
        ret += " ".join(map(str, self.rank))
        return ret
