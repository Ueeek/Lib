from collections import defaultdict
import heapq


class Dijkstra:
    """
    dijkstraの最短経路問題を解く
    input:
        S: start node
        mat : mat[a][b] = edge_weight(a,b)
    """

    def __init__(self, start, num_node, mat):
        """
        mat: mat[a][b] = edge_weight(a,b)
        num_node: num of nodes
        dist: dist from start_node
        prev: 最短経路において、一つ前のノードを記憶。経路復元に使う?
        """
        self.start_node = start
        self.mat = mat
        self.num_node = num_node
        self.dist = [float('inf')]*num_node
        self.prev = defaultdict(lambda: None)

        # dist form S to S = 0
        self.dist[start] = 0

    def calc_dist(self):
        """
        最短経路 distを計算する
        Q: content (dist_from_start,node)
        Qはheapqとして使う。dist_from_startの小さい順になる
        """
        Q = []
        heapq.heappush(Q, (0, self.start_node))
        while Q:
            dist_to_node, node = heapq.heappop(Q)
            # 現在の値よりも大きくて、更新にならない場合
            if self.dist[node] < dist_to_node:
                continue

            # 次のホップを計算する
            for nex in range(self.num_node):
                weight = self.mat[node][nex]
                cand = dist_to_node + weight

                if self.dist[nex] > cand:  # update
                    self.dist[nex] = cand
                    self.prev[nex] = node
                    heapq.heappush(Q, (cand, nex))

    def get_dist(self, d):
        """
            startからdまでの距離を返す
            これの前にcalc()を実行しておく
            たどり着けない場合は、float('inf')がかえる
        """
        return self.dist[d]
