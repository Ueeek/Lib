class MinCostFlow:
    """
    最小費用流問題
    (ある流量Fを流した時のcostの最小値を求める)
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
        #最短路の前のnodeを記録する。
        prevv=[0]*self.V #prev_node id
        preve=[0]*self.V #prev_edge id to reach prev_node

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
                #最短路のうち、min_capacity分を流す
                d = min(d, self.adj[prevv[v]][preve[v]][1])
                v = prevv[v]
            f -=d

            res += d*dist[t]

            v=t
            #流した分だけ、capacityを更新する
            while v!=s:
                e = self.adj[prevv[v]][preve[v]]
                e[1]-=d
                self.adj[v][e[3]][1]+=d

                v = prevv[v]

        return res
                



"""
# Memo
## テク
* s->gにinfの辺を張る
* 最大化の時、edge_costを(INF-val)にして、答えは、(FLOW*INF-min_cost_flow(s,g,FLOW))


##重み付き2部マッチング
* https://atcoder.jp/contests/abc195/submissions/20923368
"""
