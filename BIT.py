class BIT:
    """
    Binary Index Tree
    ###1-origin####

    add :L[i]+=x
    sum: sum(L[:l])
    range_sum : sum(L[l:r])

    #material http://hos.ac/slides/20140319_bit.pdf
    """

    init_val: int
    size: int
    L: list[int]

    def __init__(self, N: int, init_val: int = 0) -> None:
        self.init_val = init_val
        self.size = N
        self.L = [init_val]*(N+1)

    def sum(self, r: int) -> int:
        """
        sum[,r)
        calc sum from L[0] to L[r-1]
        """
        ret = self.init_val
        while r > 0:
            ret += self.L[r]
            r -= r & (-r)

        return ret

    def range_sum(self, l: int, r: int) -> int:
        """
        idx周りが怪しい?
        sum[l,r)
        calc sum from L[l] to L[r-1]
        """
        return self.sum(r-1)-self.sum(l-1)

    def add(self, i: int, x: int) -> None:
        """
        L[i] += x
        """
        while i <= self.size:
            self.L[i] += x
            i += i & (-i)

    def bisect(self, k: int) -> int:
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

# sample_　転倒数
#N = int(input())
#A = list(map(int,input().split()))
#
#B = BIT(N)
#K = 0
# for i in range(N):
#    K += i - B.sum(A[i]+1)
#    B.add(A[i]+1,1)
