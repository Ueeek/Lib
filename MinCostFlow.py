INF=10**18
class MinCostFlow:
    """
    """

    def __init__(self,V:int):
        """
        Arguments:
            V: num of vertex
        Attributes:
            self.V: num of vertex
            self.adj: adjedscent list (tuple of (to_id, capacity, cost ,rev_id))
        """
        self.INF=10**18
        self.V=V
        self.adj=[[] for _ in range(V)]


    def add_edge(self,fro:int, to:int, cap:int, cost:int):
        """
            adj[fro]=[to,cap,cost,rev]
        """
        self.adj[fro].append([to, cap,cost,len(self.adj[to])]) #edge
        self.adj[to].append([fro, 0,-cost,len(self.adj[fro])-1]) #rev_edge

    def minCostFlow(self,s:int,t:int,f:int)->int:
        """
        calculate minCost Flow
        Arguments:
            s: start node
            t: goal node
            f: flow
        """

        res=0
        #最短路の前のedgeを記録する。
        prevv=[0]*self.V
        preve=[0]*self.V

        V = self.V

        #bellman-fordで、s-tの最短路を求める
        while f>0:
            dist=[self.INF]*V
            dist[s]=0
            update = True
            while update:
                update = False
                for v in range(V):
                    if dist[v]==self.INF:
                        continue

                    for i, (to, cap, cost, _) in enumerate(self.adj[v]):
                        if cap>0 and dist[to]>dist[v]+cost:
                            dist[to]=dist[v]+cost
                            prevv[to]=v
                            preve[to]=i
                            update=True


            if dist[t]==self.INF:
                return -1

            d = f
            v = t
            while v!=s:
                d = min(d, self.adj[prevv[v]][preve[v]][1])
                v = prevv[v]

            f -=d
            res += d*dist[t]

            v=t
            while v!=s:
                e = self.adj[prevv[v]][preve[v]]
                e[1]-=d
                self.adj[v][e[3]][1]+=d

                v = prevv[v]

        return res
                

