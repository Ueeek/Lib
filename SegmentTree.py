class SegmentTree():
    '''
    非再帰
    segment tree
    '''

    def __init__(self, n:int, func=lambda x,y:max(x,y), init=float('inf')):
        '''
        n->配列の長さ
        func:func(a,b)->val,　func=minだとRMQになる
        木の高さhとすると,
        n:h-1までのノード数。h段目のノードにアクセスするために使う。
        data:ノード。data[0]:root<-leaf:data[-1]
        parent:k->child k*2+1とk*2+2
        '''
        self.n = 2**(n-1).bit_length()
        self.init = init
        self.data = [init]*(2*self.n)
        self.func = func

    def set(self, i:int, v:int):
        '''
        leafの初期化
        i: 0-origin idx
        v: value
        '''
        self.data[i+self.n-1] = v

    def set_list(self,A:list):
        """
        leafの初期化
        list_version
        """
        for i,a in enumerate(A):
            self.set(i,a)

    def build(self):
        '''
        setの後に一斉更新
        '''
        #leaf->rootに向かって、apply func していく
        for k in reversed(range(self.n-1)):
            self.data[k] = self.func(self.data[k*2+1], self.data[k*2+2])

    def update(self, k:int, a:int):
        '''
        data[k]=aに更新する。
        更新をrootまで更新
        '''
        k += self.n-1 #k=segTree上での k-th leafのidx
        self.data[k] = a

        while k > 0: #while not reach to root
            k = (k-1)//2 #goto its parent
            self.data[k] = self.func(self.data[k*2+1], self.data[k*2+2]) #update

    def query(self, l=None,r=None):
        '''
        [l,r)のfuncを求める
        '''
        if l is None:
            l=0
        if r is None:
            r=self.n
        L = l+self.n
        R = r+self.n
        ret = self.init
        while L < R:
            if R & 1: #R%2==1 
                R -= 1
                ret = self.func(ret, self.data[R-1]) #親が丸々区間に含まれない->はみ出したところを更新
            if L & 1:
                ret = self.func(ret, self.data[L-1])
                L += 1
            L >>= 1 #to parent
            R >>= 1
        return ret


    def lower_bound_index(self,x:int,v:int):
        """
        x:0-origin
        [x,N)の範囲で、v<=data[j]を満たす最小のjを探す(二分探索)

        存在しないなら、float("inf")をreturn している。
        """
        #区間の左端
        x+=self.n-1

        #data[x]が、v以上なるまで登る
        while self.data[x]<v:
            if x%2==0: #xが右のnodeなら、候補外になる
                if len(bin(x+1))==len(bin(x+2)):#一つ右に移動できるなら
                    x+=1
                else:#右に行けない->とりま大きい値をreturnしとく。(多分、全ての値が条件を満たさない時に、無限whileするのを防ぐ
                    return float("inf")

            else:#登る
                x>>=1

        # v<=data[x]を満たすように、できるだけ左(idxが小さい)に降る
        while x<self.n-1:#どこかの葉にたどり着くまで
            if self.data[2*x+1]>=v:#左の子が v<=data[x]を満たすなら、優先して左に。
                x=2*x+1
            else:#シャーなしの右
                x=2*x+2
        return x-self.n+1 #seg木のidxから、元のlistのidxに変換

    def __str__(self):
        """
        print data_array(leaf of tree)
        """
        ret=""
        for i in range(self.n):
            ret+="{} ".format(self.data[i+self.n-1])
        return ret

    def __getitem__(self,key):
        """
        print data_array[i](lead of tree)
        """
        return self.data[key+self.n-1]
