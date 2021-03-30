# -*- coding: utf-8 -*-
class FactMod():
    '''
    modの値が素数の時のfactと組み合わせを求める
    フェルマーの小定理を用いているため、modが素数以外の時は使えない

    NとかRの値が固定なら、combとか、複数回呼び出すより先に、計算してしまってlistとかで持っておく方が良い。(TLE対策)
    '''

    def __init__(self, n, mod):
        '''
        コンストラクタ
        f:nまでの i!の値を　配列に入れる
        inv_f: (i!)^-1　の値を配列に入れる
        '''
        self.mod = mod
        self.f = [1]*(n+1)
        for i in range(1, n+1):
            self.f[i] = self.f[i-1]*i % mod

        self.inv_f = [pow(self.f[-1], mod-2, mod)]
        for i in range(1, n+1)[::-1]:
            self.inv_f.append(self.inv_f[-1]*i % mod)
        self.inv_f.reverse()

    def fact(self, n):
        '''
        n!の値を返す
        '''
        assert n>=0
        return self.f[n]

    def comb(self, n, r):
        '''
        nCrの値を返す
        '''
        #assert n>=r>=0
        if r==0:
            return 1
        ret = self.f[n] * self.inv_f[n-r]*self.inv_f[r]
        ret %= self.mod
        return ret

    def perm(self, n, r):
        """
        nPrの値を返す
        """
        assert n>=r>=0
        ret = self.f[n] * self.inv_f[n-r]
        ret %= self.mod
        return ret

    def div(self,x,y):
        """
        x/yの値を返す
        このclassにいるべきじゃないな
        """
        return (x*pow(y,self.mod-2,self.mod))%self.mod

    def comb_low_r(self,n,r,MOD):
        """
        nCr=\frac{\Pi_{i=0}^{i=r-1}(n-i)}{\Pi_{i=1}^{i=r}(i)}
            FactMod(N,MOD)のNの値が大きいと、前計算が重くて、動かない。
            nCrのrが小さいという保証があるなら、以下のコードでも、十分早いはず
        """
        ret=1
        for i in range(r):#分子の計算
            ret*=(n-i)
            ret%=MOD
        for i in range(2,r+1):#分母の計算(powでinv(i)を求める。)
            ret*=pow(i,MOD-2,MOD)
            ret%=MOD
        return ret

