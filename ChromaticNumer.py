def ChromaticNunber(matrix):
    """
    グラフの彩色数を求める(隣接したノードを同じ色で塗らない。とした時に、グラフを塗る最小の色数

    Arguments:
        matrix: N*N matrix 1. matix[i][j]==1 if edge exists (i,j)(bi-directional graph)
        graph may not be connected

    Return:
        ret: chromaticNumber
    """

    N = len(matrix)

    # adj[i]: num, if num>>j&1: edge(i,j) exists
    adj=[0]*N

    for i in range(N):
        for j in range(N):
            if matrix[i][j]==1:
                adj[i]|=1<<j


    ret = N
    for d in [7,11,21]:
        mod = 10**9+d
        ind=[0]*(1<<N) #ind[S]: Sの部分集合で、独立集合をなすものの個数
        aux=[1]*(1<<N) #aux[S]: Sの彩色数?

        ind[0]=1
        for S in range(1,1<<N):
            # u: tailing consequtive zeros
            u=0
            while S&(1<<u)==0:
                u+=1
            ind[S] = ind[S^(1<<u)] + ind[(S^(1<<u))& (~adj[u])]

        i=1
        while i<ret:
            all_cnt = 0 #彩色多項式(i色で塗るときの通り数)
            for j in range(1<<N):
                S = j^(j>>1)
                aux[S]=(aux[S]*ind[S])%mod
                all_cnt += aux[S] if (j&1) else mod-aux[S] # 包除定理してる
            if all_cnt%mod: #彩色多項式は大きくなりがちなので、modでやる
                ret = i
            i+=1
    return ret


if __name__=="__main__":
    #test https://judge.yosupo.jp/problem/chromatic_number
    N,M = map(int,input().split())
    matrix=[[0]*N for _ in range(N)]
    for _ in range(M):
        a,b = map(int,input().split())
        matrix[a][b]=1
        matrix[b][a]=1

    ret = ChromaticNunber(matrix)
    print(ret)


