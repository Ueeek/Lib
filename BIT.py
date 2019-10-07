class BIT:
    """
    Binary Index Tree

    add :L[i]+=x
    sum: sum(L[:l])
    range_sum : sum(L[l:r])
    """

    def __init__(self, N, init_val=0):
        self.size = N
        self.L = [init_val]*(N+1)

    def sum(self, r):
        """
        calc sum from L[0] to L[r-1]
        """
        ret = 0
        while r > 0:
            ret += self.L[r]
            r -= r & (-r)

        return ret

    def range_sum(self, l, r):
        """
        calc sum from L[l] to L[r-1]
        """
        return self.sum(r)-self.sum(l)

    def add(self, i, x):
        """
        L[i] += x
        """
        while i < self.size:
            self.L[i] += x
            i += i & (-i)
