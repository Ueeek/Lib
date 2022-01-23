from collections import defaultdict
import heapq


class Dijkstra:
    """
    dijkstraの最短経路問題を解く
    input:
        S: start node
        adj: adj[a]=[(b,dist)]//なんとなく
    """

    def __init__(self, start, num_node, adj):
        """
        adj: adj[a]=[(b,dist)]
        num_node: num of nodes
        dist: dist from start_node
        num_shortest: そのノードに到達する最短路の数
        prev: 最短経路において、一つ前のノードを記憶。経路復元に使う?
        """
        self.start_node = start
        self.adj= adj
        self.num_node = num_node
        self.dist = [float('inf')]*num_node
        self.prev = defaultdict(lambda: None)
        self.num_shortest = [0]*num_node

        # dist form S to S = 0
        self.dist[start] = 0
        self.num_shortest[start]=1

    def calc_dist(self):
        """
        最短経路 distを計算する
        Q: content (dist_from_start,node)
        Qはheapqとして使う。dist_from_startの小さい順になる
        Qには、dist*N+nodeを入れることで高速化
        """
        Q = []
        heapq.heappush(Q, self.start_node)
        while Q:
            dist_to_node, node = divmod(heapq.heappop(Q),self.num_node)
            # 現在の値よりも大きくて、更新にならない場合
            if self.dist[node] < dist_to_node:
                continue

            # 次のホップを計算する
            for nex,weight in self.adj[node]:
                cand = dist_to_node + weight

                if self.dist[nex] > cand:  # update
                    self.dist[nex] = cand
                    self.prev[nex] = node
                    self.num_shortest[nex] = self.num_shortest[node]
                    heapq.heappush(Q, cand*self.num_node+nex)
                elif self.dist[nex]==cand:
                    self.num_shortest[nex] += self.num_shortest[node]
                    #TODO maybe this value be large

    def get_dist(self, d):
        """
            startからdまでの距離を返す
            これの前にcalc()を実行しておく
            たどり着けない場合は、float('inf')がかえる
        """
        return self.dist[d]
    def get_path(self,dst):
        """
        startからdstまでのpathをlistでreturn
        valifyしてないので怪しい
        """
        if self.dist[dst]==float("inf"):
            return []
        cur=dst
        ret=[cur]
        while cur!=self.start_node:
            cur=self.prev[cur]
            ret.append(cur)
        return list(reversed(ret))
