# ref http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=3986599#1
class Lazy_SegTree:
    """
    Lazy Segment Tree
        * handle range update
    """

    def __init__(self, n, func, init=float('inf')):
        """__init__
        :param
            n: size of node
            func: merge func
            init: initial value of each nde
        """
        self._n = n
        self.n = 2**(n-1).bit_length()
        self.init = init
        self.data = [init]*(2*self.n)
        self.lazy = [None]*(2*self.n)
        self.func = func

    def set(self, pos, val):
        """set

        :param pos: position of value
        :param val: set value
        """
        self.data[pos+self.n-1] = val

    def build(self):
        """build
            called after set, build initial seg tree
        """
        for k in reversed(range(self.n-1)):
            self.data[k] = self.func(self.data[k*2+1], self.data[k*2+2])

    def _update_range(self, l, r):
        """_update_range
            get range of updated nodes

        :param l:
        :param r:
        """
        L = l+self.n
        R = r+self.n

        lm = (L//(L & -L)) >> 1
        rm = (R//(R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1
            R >>= 1
        while L:
            yield L
            L >>= 1

    def _propagates(self, *ids):
        """_propagates
            propagete lazy-value

        :param *ids:
        """
        for i in reversed(ids):
            v = self.lazy[i-1]
            if v is None:
                continue
            self.lazy[2*i-1] = \
                self.data[2*i-1] = self.lazy[2*i] = self.data[2*i] = v
            self.lazy[i-1] = None

    def update(self, l, r, x):
        """update
            update values [l,r) with x
        :param l: left index
        :param r: right index
        :param x: value
        """
        *ids, = self._update_range(l, r)
        self._propagates(*ids)
        L = l+self.n
        R = r + self.n
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] = self.data[R-1] = x
            if L & 1:
                self.lazy[L-1] = self.data[L-1] = x
                L += 1
            L >>= 1
            R >>= 1
        for i in ids:
            self.data[i-1] = self.func(self.data[2*i-1], self.data[2*i])

    def query(self, l, r):
        """query
            return value [l,r)
        :param l: left index
        :param r: right index
        """
        self._propagates(*self._update_range(l, r))
        L = l + self.n
        R = r + self.n
        ret = self.init

        while L < R:
            if R & 1:
                R -= 1
                ret = self.func(ret, self.data[R-1])
            if L & 1:
                ret = self.func(ret, self.data[L-1])
                L += 1
            L >>= 1
            R >>= 1
        return ret

    def print_tree(self):
        print(" ".join(map(str, [self.data[i+self.n-1]
                                 for i in range(self._n)])))
