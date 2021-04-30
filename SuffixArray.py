from collections import Counter
import bisect


class SuffixArray:
    "not verified. yosupo judge見てTODO"
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
        壊れてる気がするから使わない
        build SA with O(N)
        SA_IS algorithm

        set self.suffix array:
            list:(index,suffix)
        """

        def build_LS_array():
            """
            """
            N = len(self.string)
            L = [0]*N
            L[-1] = "S"
            for i in reversed(range(N-1)):
                if self.string[i] > self.string[i+1]:
                    L[i] = "L"
                elif self.string[i] < self.string[i+1]:
                    L[i] = "S"
                else:
                    L[i] = L[i+1]
            return L

        def find_lmss(LS, cheat=False):
            """
            return set of LMS
            """
            N = len(self.string)
            LMS = [i for i in range(1, N) if LS[i-1] == "L" and LS[i] == "S"]
            if cheat:
                LMS = sorted(LMS, key=lambda x: self.string[x:], reverse=False)
                print("LMS=>", LMS)
            return LMS

        def induced_sort(LS, lmss):
            suffix_array = [None]*N
            C = Counter(self.string)
            bin_start = dict()
            bin_cnt = dict()
            tmp = 0
            for key, val in sorted(C.items(), key=lambda x: x[0]):
                bin_cnt[key] = 0
                bin_start[key] = tmp
                tmp += val

            for i in reversed(lmss):
                c = self.string[i]
                suffix_array[bin_start[c]+C[c]-bin_cnt[c]-1] = i
                bin_cnt[c] += 1

            for key, val in bin_cnt.items():
                bin_cnt[key] = 0
            for e in suffix_array:
                if e is None or e == 0 or LS[e-1] == "S":
                    continue
                ch = self.string[e-1]
                suffix_array[bin_start[ch]+bin_cnt[ch]] = e-1
                bin_cnt[ch] += 1

            for key, val in bin_cnt.items():
                bin_cnt[key] = 0
            for e in reversed(suffix_array):
                if e is None or e == 0 or LS[e-1] == "L":
                    continue
                ch = self.string[e-1]
                suffix_array[bin_start[ch]+C[ch]-bin_cnt[ch]-1] = e-1
                bin_cnt[ch] += 1
            return suffix_array

        N = len(self.string)
        suffix_array = [None]*N
        LS = build_LS_array()
        LMS = find_lmss(LS, cheat=True)
        suffix_array = induced_sort(LS, LMS)

        name = 0
        prev = -1
        pLMS = {}
        for e in suffix_array:
            if e in LMS:
                for i in range(N):
                    if prev == -1 or self.string[e+i] != self.string[prev+i]:
                        name += 1
                        prev = e
                        break
                    elif i and (e+i in LMS or prev+i in LMS):
                        break
                pLMS[e] = name-1

        if name < len(LMS):
            sublst = [pLMS[e] for e in LMS if e < N-1]
            print("SUBLST=>", sublst)
        else:
            LMS = [e for e in reversed(suffix_array) if e in LMS]
        return induced_sort(LS, LMS)

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
        match_pos = list(range(l, r+1))
        for i in match_pos:
            print("match=>", self.string[i:])
        return match_pos


if __name__ == "__main__":
    S = input()
    SA = SuffixArray(S)
    #SA.build_suffix_array_naive()
    #SA.build_suffix_array_manber_mayers()
    SA.build_suffix_array_sa_is()

    ans = []
    for pos,val in SA.suffix_array[1:]:
        ans.append(pos)
    print(" ".join(map(str,ans)))
