from collections import defaultdict
from math import sqrt, ceil
import sys
input = sys.stdin.readline


class Mo:
    """
    updateがない
    queryを先読みできる
    区間に何種類のものがある?みたいな時に使いやすそう
    """

    def __init__(self, L):
        self.L = L
        self.N = len(L)
        self.bucket_size = ceil(sqrt(self.N))

    def _init_states(self):
        """
        state: information you wannna know for each euqry
        """

        self.states = None
        self.n_unique = 0
        self.cnt = defaultdict(int)

        # [l,r) (r.exclusize)
        self.l = 0
        self.r = 0

        # queries
        self.bucket = [[] for _ in range(self.bucket_size+1)]

    def _add(self, i):
        """
         add i-th element  and update state

         write this operation  by your self 
        """
        raise NotImplementedError

        if self.cnt[self.L[i]] == 0:
            self.n_unique += 1
        self.cnt[self.L[i]] += 1

    def _delete(self, i):
        """
         delete  ith element and update state
         write this operation by your self
        """

        raise NotImplementedError

        self.cnt[self.L[i]] -= 1
        if self.cnt[self.L[i]] == 0:
            self.n_unique -= 1

    def _one_process(self, l, r):
        """
        update state for each euqry(l,r)
        """
        for i in range(self.r, r):  # extend to r
            self._add(i)

        for i in range(self.r-1, r-1, -1):  # shorten to r <= Rでsortしてるからいらなくね?なんかWA生えた
            self._delete(i)

        for i in range(self.l, l):
            self._delete(i)

        for i in range(self.l-1, l-1, -1):
            self._add(i)

        self.l = l
        self.r = r

    def process(self, queries):
        """
        Argument:
            queries:list([l,r)] r is exclusive
        Return:
            ans:ans[i] is answwer for i-th querry
        """
        self._init_states()

        for i, (l, r) in enumerate(queries):
            self.bucket[l//self.bucket_size].append((l, r, i))

        # sort each bucket content by r
        for i in range(len(self.bucket)):
            self.bucket[i].sort(key=lambda x: x[1])

        ans = [None]*len(queries)

        for b in self.bucket:
            for l, r, i in b:
                self._one_process(l, r)
                raise NotImplementedError
                ans[i] = self.n_unique
        return ans


# code of https://atcoder.jp/contests/abc174/submissions/me
N, Q = map(int, input().split())
L = list(map(int, input().split()))

M = Mo(L)

queries = []
for _ in range(Q):
    l, r = map(lambda x: int(x)-1, input().split())
    queries.append((l, r+1))

ans = M.process(queries)
print("\n".join(map(str, ans)))
