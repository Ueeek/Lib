import bisect


class SuffixArray:
    """
    Suffix Array:
        search query words from sentences
    """

    def __init__(self, string, pattern="$"):
        """
        string: search query from this string
        pattern: banpei
        """
        self.string = string+pattern
        self.pattern = pattern
        self.suffix_array = None

    def build_suffix_array_sa_is(self):
        """
        build SA with O(N)
        SA_IS algorithm

        set self.suffix array:
            list:(index,suffix)
        """
        pass

    def build_suffix_array_manber_mayers(self):
        """
        build SA with O(N(log(N)**2) )
        manber&mayers algorithm

        set self.suffix array:
            list:(index,suffix)
        """
        N = len(self.string)
        suffix_array = list(range(N))
        rank = [c for c in self.string]
        sa_tmp = [0]*N
        k = 1

        def compare_key(x):
            """
            key function for sort
            compare two and return 1 or -1
            """
            return (rank[x], rank[x+k] if x+k < N else -1)
        while k <= N:  # use doubling to reduce compare cost of two strings from N to logN)
            suffix_array = sorted(suffix_array, key=compare_key)
            sa_tmp[suffix_array[0]] = 0
            for i in range(1, N):
                sa_tmp[suffix_array[i]] = sa_tmp[suffix_array[i-1]] +\
                    (compare_key(suffix_array[i-1])
                     < compare_key(suffix_array[i]))

            rank = sa_tmp
            k <<= 1
        self.suffix_array = [(v, self.string[v:]) for v in suffix_array]

    def build_suffix_array_naive(self):
        """
        build SA with O(N**2log(N)) naive way
        set self.suffix array:
            list:(index,suffix)
        """
        suffix_array = []
        for i in range(len(self.string)):
            suffix_array.append((i, self.string[i:]))

        self.suffix_array = list(sorted(suffix_array, key=lambda x: x[1]))

    def search(self, query):
        """
        * search query words from string
        * return
            * start positions of query in self.string
        """
        query += self.pattern
        l = bisect.bisect_left([v[1] for v in self.suffix_array], query)
        r = bisect.bisect_right([v[1] for v in self.suffix_array], query)
        match_pos = [list(range(l, r+1))]
        return match_pos


if __name__ == "__main__":
    S = "nonsense"
    SA = SuffixArray(S)
    SA.build_suffix_array_naive()
    print("naive=>", SA.suffix_array)
    SA.build_suffix_array_manber_mayers()
    print("manver_mayers=>", SA.suffix_array)
    ret = SA.search("nse")
    print(ret)
