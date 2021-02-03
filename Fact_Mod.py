# -*- coding: utf-8 -*-
class FactMod():
    '''
    modの値が素数の時のfactと組み合わせを求める
    フェルマーの小定理を用いているため、modが素数以外の時は使えない
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
        return self.f[n]

    def comb(self, n, r):
        '''
        nCrの値を返す
        '''
        ret = self.f[n] * self.inv_f[n-r]*self.inv_f[r]
        ret %= self.mod
        return ret

    def perm(self, n, r):
        """
        nPrの値を返す
        """
        ret = self.f[n] * self.inv_f[n-r]
        ret %= self.mod
        return ret

    def div(self,x,y):
        """
        x/yの値を返す
        """
        return (x*pow(y,self.mod-2,self.mod))%self.mod

