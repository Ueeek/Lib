class BIT:
    """
    Binary Index Tree
    ###1-origin####

    add :L[i]+=x
    sum: sum(L[:l])
    range_sum : sum(L[l:r])

    #material http://hos.ac/slides/20140319_bit.pdf
    """

    def __init__(self, N, init_val=0):
        self.init_val = init_val
        self.size = N
        self.L = [init_val]*(N+1)

    def sum(self, r):
        """
        sum[,r)
        calc sum from L[0] to L[r-1]
        """
        ret = self.init_val
        while r > 0:
            ret += self.L[r]
            r -= r & (-r)

        return ret

    def range_sum(self, l, r):
        """
        idx周りが怪しい?
        sum[l,r)
        calc sum from L[l] to L[r-1]
        """
        return self.sum(r-1)-self.sum(l-1)

    def add(self, i, x):
        """
        L[i] += x
        """
        while i <= self.size:
            self.L[i] += x
            i += i & (-i)

    def bisect(self, k: float) -> int:
        """ binary search on BIT
        get index x s.t self.sum(,)>=k

        RETURN:
            res:index of x
        """
        k += 1  # convert k into 1-index

        res = 0
        N = 1
        while N < self.size:
            N *= 2

        i = N//2
        while i > 0:
            # move to rignt on tree
            if(res+i < self.size and self.L[res+i] < k):
                k -= self.L[res+i]
                res += i
            # else move to left
            i //= 2
        return res+1
