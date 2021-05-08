class Tree:
    """
    木のアルゴリズムまとめたクラス
    """

    def __init__(self,N):
        self.parent=[[] for _ in range(N)]
        self.parent=None
        self.child=None
        self.topological_order=None
        self.root=None

    def set_root(self,root):
        if self.root is None:
            self.root=root
        else:
            print("root is already setted")


    def add_edge(self,a,b):
        self.adj[a].append(b)
        self.adj[b].append(a)

    def topological_sort(self):
        pass
    
    def calc_diameter(self):
        pass

    def lca(self,a,b):
        pass
